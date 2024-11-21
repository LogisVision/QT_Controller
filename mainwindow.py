import sys
import paho.mqtt.client as mqtt
import torch  # YOLOv5를 위해 필요
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QUrl, QTimer, QThread, Signal,QRect
from ui_form import Ui_MainWindow  # Import the generated UI file
import cv2
import numpy as np
import json
from datetime import datetime
import pytz
import platform, pathlib
from pathlib import Path

# 한국 시간대 설정
korea_timezone = pytz.timezone("Asia/Seoul")

# 브로커(라즈베리파이) 아이피 주소
address = "172.20.10.9"
port = 1883

# MQTT Topics
commandTopic = "AGV/command"
sensingTopic = "AGV/sensing"
cameraTopic = "AGV/camera"
autoTopic = "AGV/auto_mode"
# 거리 계산을 위한 상수
KNOWN_WIDTH = 3.0  # 객체의 실제 너비 (cm)
FOCAL_LENGTH = 389.12  # IMX219-160 기반 초점 거리 (픽셀)

# YOLOv5 모델 로드
plt = platform.system()
if plt == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath
else:
    pathlib.WindowsPath = pathlib.PosixPath
model = Path("best.pt")


model_path = "best.pt"  # 모델 경로를 지정
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

# GPU 사용 설정
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # GPU or CPU 선택
# model.to(device)  # 모델을 선택한 장치로 이동
# model.conf = 0.3  # 감지 임계값 설정


# YOLO 처리 스레드
frame_queue = []
processed_frame_queue = []

class VideoProcessingThread(QThread):
    frame_processed = Signal(np.ndarray, np.ndarray)  # 처리된 결과와 원본 프레임을 전달

    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.running = True

    def run(self):
        while self.running:
            if frame_queue:
                frame = frame_queue.pop(0)  # 원본 프레임 가져오기
                frame_resized = cv2.resize(frame, (640, 480))  # YOLO 모델 입력 크기로 리사이즈
                results = self.model(frame_resized)  # YOLO 처리
                self.frame_processed.emit(results.xyxy[0].numpy(), frame)  # 결과와 원본 프레임 반환

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

        self.video_thread = VideoProcessingThread(model)
        self.video_thread.frame_processed.connect(self.process_results)
        self.video_thread.start()
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_ui_frame)
        self.update_timer.start(33)

        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.connect(address, port)
        self.client.subscribe(cameraTopic)
        self.client.loop_start()


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


        self.auto_mode_active = False
        # 타이머 설정

        # --- QWebEngineView 생성 및 초기 설정 ---
        self.web_view = QWebEngineView(self.ui.widget_web)  # Create the QWebEngineView
        self.web_view.setUrl("https://www.google.com")  # Set the initial URL
        self.web_view.show()

        # --- 주소창 연결 ---
        self.ui.lineEdit_url.returnPressed.connect(self.load_url)  # Enter 키로 URL 로드
        self.ui.lineEdit_url.setText("https://www.google.com")  # 기본 URL 표시
        self.ui.btn_url_enter.clicked.connect(self.web_go)  # Enter 버튼 클릭 연결

        # --- 초기 실행 시 widget_web 크기를 기반으로 WebView 설정 ---
        self.update_webview_geometry()  # Ensure initial size matches widget_web

    def resizeEvent(self, event):
        """Update the geometry of the QWebEngineView when widget_web is resized."""
        super().resizeEvent(event)  # Call the parent class resizeEvent
        self.update_webview_geometry()

    def update_webview_geometry(self):
        """Synchronize the QWebEngineView geometry with widget_web."""
        widget_geometry = self.ui.widget_web.geometry()  # Get the current geometry of widget_web
        # Update QWebEngineView geometry to match widget_web
        self.web_view.setGeometry(QRect(0, 0, widget_geometry.width(), widget_geometry.height()))

    def web_prev(self):
        if self.web_view.history().canGoBack():
            self.web_view.back()

    def web_next(self):
        if self.web_view.history().canGoForward():
            self.web_view.forward()

    def web_refresh(self):
        self.web_view.reload()

    def web_go(self):
        url = self.ui.lineEdit_url.text()  # Get text from the address bar
        if url:  # If the URL is not empty
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url  # Add "https://" if not present
            self.web_view.setUrl(url)  # Load the URL in the web view

   # --- 주소창 URL 로드 함수 ---
    def load_url(self):
        """Load the URL from the lineEdit_url into the WebView."""
        url = self.ui.lineEdit_url.text()  # Get text from the address bar
        if url:  # If the URL is not empty
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url  # Add "https://" if not present
            self.web_view.setUrl(url)  # Load the URL in the web view




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
        if msg.topic == cameraTopic:
                jpg_as_np = np.frombuffer(msg.payload, dtype=np.uint8)
                frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)
                if frame is not None:
                    frame_queue.append(frame)

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

    def process_results(self, detections, frame):
        try:
            for det in detections:
                x_min, y_min, x_max, y_max, confidence, cls = det
                if confidence < 0.5:
                    continue
                # 바운딩 박스 그리기
                cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
                cv2.putText(frame, f"Conf: {confidence:.2f}", (int(x_min), int(y_min) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # 처리된 프레임을 큐에 추가
            processed_frame_queue.append(frame)

        except Exception as e:
            print(f"Error in process_results: {e}")

    def update_ui_frame(self):
        if processed_frame_queue:
            frame = processed_frame_queue.pop(0)
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            qt_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
            self.ui.label_cam.setPixmap(QPixmap.fromImage(qt_image))


    def process_label_cam(self, payload):
            try:
                # MQTT로부터 수신한 이미지 디코딩
                jpg_as_np = np.frombuffer(payload, dtype=np.uint8)
                frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)
                if frame is None:
                    print("Failed to decode frame.")
                    return

                # YOLOv5로 객체 감지
                frame_resized = cv2.resize(frame, (640, 480))  # YOLO 모델이 더 작은 해상도에서 실행
                results = model(frame)
                detections = results.xyxy[0].numpy()  # 결과를 numpy 배열로 변환

                # QLabel 크기 (중심 계산용)
                widget_width = self.ui.label_cam.width()
                widget_height = self.ui.label_cam.height()

                for det in detections:
                    x_min, y_min, x_max, y_max, confidence, cls = det
                    if confidence < 0.5:  # 신뢰도 필터링
                        continue

                    # 클래스 이름 가져오기
                    class_name = model.names[int(cls)]

                    # 바운딩 박스 좌표 제한 (QLabel 경계 안으로)
                    x_min = max(0, int(x_min))
                    y_min = max(0, int(y_min))
                    x_max = min(widget_width - 1, int(x_max))
                    y_max = min(widget_height - 1, int(y_max))

                    # 바운딩 박스 그리기
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                    cv2.putText(frame, f"{class_name} {confidence:.2f}", (x_min, y_min - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                    # 거리 계산
                    w = x_max - x_min
                    distance_cm = (KNOWN_WIDTH * FOCAL_LENGTH) / w
                    cv2.putText(frame, f"{distance_cm:.2f} cm", (x_min, y_min - 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

                    # MQTT 송신
                    if self.auto_mode_active:
                        target_center_x = x_min + w // 2
                        target_center_y = y_min + (y_max - y_min) // 2
                        offset_x = target_center_x - widget_width // 2
                        offset_y = widget_height // 2 - target_center_y
                        movement_data = {"x": offset_x, "y": offset_y}
                        self.client.publish(autoTopic, json.dumps(movement_data))
                        print(f"Sent offset data: {movement_data}")

                # OpenCV → QLabel 변환
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
