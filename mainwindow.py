import sys
import paho.mqtt.client as mqtt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QTableWidget, QTableWidgetItem, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QUrl, QTimer, QThread, Signal
from ui_form import Ui_MainWindow  # Import the generated UI file
import cv2
import numpy as np
import json
from datetime import datetime
import pytz

# 한국 시간대 설정
korea_timezone = pytz.timezone("Asia/Seoul")

# 브로커(라즈베리파이) 아이피 주소
address = "70.12.225.174"
port = 1883

# MQTT Topics
commandTopic = "AGV/command"
sensingTopic = "AGV/sensing"
cameraTopic = "AGV/camera"
autoTopic = "AGV/auto_mode"
# 거리 계산을 위한 상수
KNOWN_WIDTH = 14.0  # 객체의 실제 너비 (cm)
FOCAL_LENGTH = 389.12  # IMX219-160 기반 초점 거리 (픽셀)




class MainWindow(QMainWindow):
    servo_angle = 0
    cam_angle = -7

    sensorData = list()  # MQTT로 받은 센서 데이터 저장
    sensingDataList = list()  # 최신 15개의 센서 데이터 저장

    commandData = dict()  # MQTT로 보낼 명령 데이터
    commandDataList = list()  # 보낸 명령 데이터 저장

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

        # 버튼 이벤트 설정
        self.ui.btn_grab.clicked.connect(lambda: self.target_grab(0, 0, 0))

        # 테이블 열 너비 설정
        self.ui.table_log.setColumnWidth(0, 150)
        self.ui.table_log.setColumnWidth(1, 80)
        self.ui.table_log.setColumnWidth(2, 80)
        self.ui.table_log.setColumnWidth(3, 70)

        self.ui.table_sensing.setColumnWidth(0, 150)
        self.ui.table_sensing.setColumnWidth(1, 80)
        self.ui.table_sensing.setColumnWidth(2, 80)
        self.ui.table_sensing.setColumnWidth(3, 80)
        self.ui.table_sensing.setColumnWidth(4, 80)

        # MQTT 클라이언트 설정
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(address, port)
        self.client.subscribe(sensingTopic, qos=1)
        self.client.subscribe(cameraTopic, qos=1)
        self.client.loop_start()

        # QWebEngineView 설정
        self.web_view = QWebEngineView(self.ui.widget_web)
        self.web_view.setGeometry(self.ui.widget_web.geometry())
        self.web_view.setUrl(QUrl("https://www.google.com"))
        self.web_view.show()

        # 객체 인식을 위한 Cascade 모델 로드
        self.target_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

        self.auto_mode_active = False
        # 타이머 설정



    def init(self):
        print("Initialized")

    def makeCommandData(self, cmd_string, arg, finish):
        current_time = datetime.now(korea_timezone)
        return {
            "time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "cmd_string": cmd_string,
            "arg_string": arg,
            "is_finish": finish,
        }

    def on_connect(self, client, userdata, flags, reason_code):
        if reason_code == 0:
            print("Connected to MQTT Broker")
        else:
            print("Failed to connect:", reason_code)

    def on_message(self, client, userdata, msg):
        if msg.topic == sensingTopic:
            try:
                data = json.loads(msg.payload.decode("utf-8"))
                self.sensorData.append(data)
                self.sensingDataList = self.sensorData[-15:]
                self.update_sensing_table()
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        elif msg.topic == cameraTopic:
            self.process_label_cam(msg.payload)

    def process_label_cam(self, payload):
        try:
            jpg_as_np = np.frombuffer(payload, dtype=np.uint8)
            frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)
            if frame is None:
                print("Failed to decode frame.")
                return

            # 객체 탐지
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            targets = self.target_cascade.detectMultiScale(
                gray_frame, scaleFactor=1.3, minNeighbors=3, minSize=(50, 50)
            )

            # QLabel의 중심 좌표 계산
            widget_width = self.ui.label_cam.width()
            widget_height = self.ui.label_cam.height()


            for (x, y, w, h) in targets:
                # 사각형 그리기
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # 객체 중심 좌표
                target_center_x = x + w // 2
                target_center_y = y + h // 2

                screen_center_x = widget_width // 2
                screen_center_y = widget_height // 2

                # 중심에서의 오프셋 계산
                offset_x = int(target_center_x - screen_center_x)
                offset_y = int(target_center_y - screen_center_y)*(-1)

                threshold_x = 1
                threshold_y = 1

                """
                # Horizontal adjustment (left/right rotation) using servo_angle
                if offset_x < -threshold_x:
                    self.servo_angle -= 1
                    if self.servo_angle < -80:  # Lower limit for horizontal servo angle
                        self.servo_angle = -80
                elif offset_x > threshold_x:
                    self.servo_angle += 1
                    if self.servo_angle > 80:  # Upper limit for horizontal servo angle
                        self.servo_angle = 80

                if offset_y < -threshold_y:
                    self.cam_angle +=1
                    if self.cam_angle > 25 :
                        self.cam_angle = 25
                elif offset_y > threshold_y:
                    self.cam_angle -=1
                    if self.cam_angle < -40:
                        self.cam_angle = -40
                """



                # 거리 계산
                distance_cm = (KNOWN_WIDTH * FOCAL_LENGTH) / w
                cv2.putText(frame, f"{distance_cm:.2f} cm", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                # Automode 활성화 상태에서 MQTT로 송신
                if getattr(self, "auto_mode_active", False):
                    movement_data = {"x": offset_x, "y": offset_y}
                    self.client.publish("AGV/auto_mode", json.dumps(movement_data))
                    print(f"Sent offset data: {movement_data}")

                # 객체 중심점 표시
                cv2.rectangle(
                    frame,
                    (target_center_x - 5, target_center_y - 5),
                    (target_center_x + 5, target_center_y + 5),
                    (0, 255, 0),
                    2,
                )
                break  # 첫 번째 객체만 처리

            # OpenCV 이미지 -> QLabel
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.ui.label_cam.setPixmap(pixmap.scaled(self.ui.label_cam.size()))
            self.ui.label_cam.setScaledContents(True)

        except Exception as e:
            print(f"Error updating label_cam: {e}")

    def set_reset(self):
        command_data = self.makeCommandData("reset", 0, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def arm_set(self):
        x = 100  # 원하는 x 좌표
        y = 50   # 원하는 y 좌표

        command_data = self.makeCommandData("move_arms",f"{x},{y}",1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def stop(self):
        command_data = self.makeCommandData("stop", 100, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.client.loop_stop()
        print(self.commandDataList)

    def send_xy_set(self, x, y):
        pass

    def mode_auto(self):
        # AUTO 버튼 활성화 시
        if self.ui.btn_auto.isChecked():
            self.ui.btn_manual.setChecked(False)  # MANUAL 버튼 비활성화
            self.auto_mode_active = True

            # MQTT로 AUTO_ON 명령 전송
            self.client.publish("AGV/control", "AUTO_ON", qos=1)
            print("Auto mode activated.")

    def mode_manual(self):
        # MANUAL 버튼 활성화 시
        if self.ui.btn_manual.isChecked():
            self.ui.btn_auto.setChecked(False)  # AUTO 버튼 비활성화
            self.auto_mode_active = False

            # MQTT로 AUTO_OFF 명령 전송
            self.client.publish("AGV/control", "AUTO_OFF", qos=1)
            print("Manual mode activated.")

    def settingUI(self):
        self.ui.table_log.setRowCount(0)
        for i, commandData in enumerate(self.commandDataList):
            row_position = self.ui.table_log.rowCount()
            self.ui.table_log.insertRow(row_position)
            self.ui.table_log.setItem(row_position, 0, QTableWidgetItem(commandData["time"]))
            self.ui.table_log.setItem(row_position, 1, QTableWidgetItem(commandData["cmd_string"]))
            self.ui.table_log.setItem(row_position, 2, QTableWidgetItem(str(commandData["arg_string"])))
            self.ui.table_log.setItem(row_position, 3, QTableWidgetItem(str(commandData["is_finish"])))

    def update_sensing_table(self):
        self.ui.table_sensing.setRowCount(0)
        for i, data in enumerate(self.sensingDataList):
            row_position = self.ui.table_sensing.rowCount()
            self.ui.table_sensing.insertRow(row_position)
            self.ui.table_sensing.setItem(row_position, 0, QTableWidgetItem(data.get("time", "")))
            self.ui.table_sensing.setItem(row_position, 1, QTableWidgetItem(str(data.get("num1", ""))))
            self.ui.table_sensing.setItem(row_position, 2, QTableWidgetItem(str(data.get("num2", ""))))
            self.ui.table_sensing.setItem(row_position, 3, QTableWidgetItem(str(data.get("is_finish", ""))))
            self.ui.table_sensing.setItem(row_position, 4, QTableWidgetItem(data.get("manual_mode", "")))


    # def turn_angle(self, offset_x):
    #     """
    #     좌우 각도 조정을 위한 turnAngle 함수 호출
    #     """
    #     # offset_x를 각도로 변환 (가중치 적용 가능)
    #     turn_value = self.servo_angle + offset_x // 10
    #     turn_value = max(min(turn_value, 80), -80)  # 각도 제한
    #     self.servo_angle = turn_value

    #     # MQTT로 turnAngle 명령 전송
    #     command_data = self.makeCommandData("camera_turn_angle", turn_value, 1)
    #     self.client.publish(commandTopic, json.dumps(command_data), qos=1)
    #     print(f"Sent turn_angle command: {turn_value}")

    # def camera_angle(self, offset_y):
    #     """
    #     상하 각도 조정을 위한 camAngle 함수 호출
    #     """
    #     # offset_y를 각도로 변환 (가중치 적용 가능)
    #     cam_value = self.cam_angle - offset_y // 10
    #     cam_value = max(min(cam_value, 25), -40)  # 각도 제한
    #     self.cam_angle = cam_value

    #     # MQTT로 camAngle 명령 전송
    #     command_data = self.makeCommandData("camera_angle", cam_value, 1)
    #     self.client.publish(commandTopic, json.dumps(command_data), qos=1)
    #     print(f"Sent camera_angle command: {cam_value}")


    def camera_angle(self, angle):
        mapped_angle = 25 - (angle + 40)
        command_data = self.makeCommandData("camera_angle", mapped_angle, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()
        print(f"Sent camera_angle command with angle: {angle}")

    def turn_angle(self, angle):
        command_data = self.makeCommandData("camera_turn_angle", angle, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()
        print(f"Sent camera_turn_angle command with angle: {angle}")

    def grab(self, angle):
       mapped_angle = angle * -1
       command_data = self.makeCommandData("grab_angle", mapped_angle, 1)
       self.client.publish(commandTopic, json.dumps(command_data), qos=1)
       self.commandDataList.append(command_data)
       self.settingUI()
       print(f"Sent grab_angle command with angle: {angle}")

    def slide_x_plus(self) :
        self.ui.slider_arm_1.setValue(self.ui.slider_arm_1.value() + 1)

    def slide_x_minus(self) :
        self.ui.slider_arm_1.setValue(self.ui.slider_arm_1.value() - 1)

    def slide_y_plus(self) :
        self.ui.slider_arm_2.setValue(self.ui.slider_arm_2.value() + 1)

    def slide_y_minus(self) :
        self.ui.slider_arm_2.setValue(self.ui.slider_arm_2.value() - 1)

    def arm_1(self, angle) :
        mapped_angle = angle#- 130
        command_data = self.makeCommandData("arm_x", mapped_angle, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def arm_2(self, angle) :
        mapped_angle = angle
        command_data = self.makeCommandData("arm_y", mapped_angle, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def go(self):
        command_data = self.makeCommandData("go", 100, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def mid(self):
        command_data = self.makeCommandData("mid", 100, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def back(self):
        command_data = self.makeCommandData("back", 100, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def left(self):
        command_data = self.makeCommandData("left", 100, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def right(self):
        command_data = self.makeCommandData("right", 100, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def target_grab(self, center_x, center_y, distance_cm):
        xy_values = f"{center_x},{distance_cm}"
        command_data = self.makeCommandData("move_arms", center_x,center_y, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def closeEvent(self, event):
        self.client.disconnect()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
