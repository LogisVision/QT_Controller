
# # Important:
# # You need to run the following command to generate the ui_form.py file
# #     pyside6-uic form.ui -o ui_form.py, or
# #     pyside2-uic form.ui -o ui_form.py
# from ui_form import Ui_MainWindow

import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QTableWidget, QTableWidgetItem, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, QUrl

import paho.mqtt.client as mqtt

# Import the generated UI file
from ui_form import Ui_MainWindow

import json
from datetime import datetime
import pytz

#한국 시간대 설정
korea_timezone = pytz.timezone("Asia/Seoul")

# 브로커(라즈베리파이) 아이피 주소
address = "70.12.225.174"
port = 1883

#MQTT command Topic
commandTopic = "AGV/command"

#MQTT Sensor Topic
sensingTopic = "AGV/sensing"

cameraTopic = "AGV/camera"


class MainWindow(QMainWindow):

    # 초기 연결 설정
    # mqtt로 들어온 data를 받아줄 list 생성
    sensorData = list()
    # sensorData 중 최신 15개 data만 저장할 list
    sensingDataList = list()

    #mqtt로 보낼 command dict
    commandData = dict()
    #commandData 전체
    commandDataList = list()



    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

        # 타이머를 사용해 주기적으로 프레임을 가져옵니다.
        #self.timer = QTimer()
        #self.timer.timeout.connect(self.update_frame)
        #self.timer.start(30)  # 30ms마다 업데이트

        # GStreamer를 사용해 네트워크 스트림에서 영상을 받아옵니다.
        #self.cap = cv2.VideoCapture(0)  # USB 카메라 또는 기본 카메라를 사용합니다.

        # log column 너비 설정
        self.ui.table_log.setColumnWidth(0, 150)  # Time 열 너비 설정
        self.ui.table_log.setColumnWidth(1, 80)  # Command 열 너비 설정
        self.ui.table_log.setColumnWidth(2, 80)  # Value 열 너비 설정
        self.ui.table_log.setColumnWidth(3, 70)   # Status 열 너비 설정

        self.ui.table_sensing.setColumnWidth(0, 150)  # Time 열 너비 설정
        self.ui.table_sensing.setColumnWidth(1, 80)  # Command 열 너비 설정
        self.ui.table_sensing.setColumnWidth(2, 80)  # Value 열 너비 설정
        self.ui.table_sensing.setColumnWidth(3, 80)   # Status 열 너비 설정
        self.ui.table_sensing.setColumnWidth(4, 80)

        # MQTT 클라이언트 생성
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
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
        #self.ui.widget_web.hide()
        self.web_view.show()


    def init(self):
        print("init")

    def load_url(self, url):
        self.web_view.setUrl(QUrl(url))

    def start(self):
        # MQTT 클라이언트 생성
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        # 연결 시 콜백 함수 설정
        self.client.on_connect = self.on_connect
        # 메시지 수신 시 콜백 함수 설정
        self.client.on_message = self.on_message

        # Broker IP, port 연결
        self.client.connect(address, port)
        self.client.subscribe(sensingTopic, qos=1)
        self.client.loop_start()

        # QTimer 설정 (0.5초마다 settingUI 메서드 호출)
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.settingUI)
        # self.timer.start(500)  # 1000ms = 1초
        # print('start')


    def makeCommandData(self, str, arg, finish):
        current_time = datetime.now(korea_timezone)
        self.commandData["time"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.commandData["cmd_string"] = str
        self.commandData["arg_string"] = arg
        self.commandData["is_finish"] = finish
        return self.commandData

    # def makeCommandData(self, cmd_string, arg, finish):
    #     current_time = datetime.now(korea_timezone)
    #     self.commandData = {
    #         "time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
    #         "cmd_string": cmd_string,
    #         "arg_string": arg,
    #         "is_finish": finish
    #     }
    #     return self.commandData

    def stop(self):
        self.commandData = self.makeCommandData("stop", 100, 1)
        self.client.publish(commandTopic, json.dumps(self.commandData), qos=1)
        self.commandDataList.append(self.commandData)
        self.commandData = dict()

        self.client.loop_stop()
        print(self.commandDataList)



    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        # OpenCV BGR 포맷을 Qt가 사용하는 RGB 포맷으로 변환
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # QPixmap으로 변환하고 QLabel의 크기에 맞게 조정
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(self.ui.label_cam.size())

        # QLabel에 QPixmap 표시
        self.ui.label_cam.setPixmap(scaled_pixmap)

    def closeEvent(self, event):
        # 프로그램 종료 시 카메라 해제
        self.cap.release()
        event.accept()

    def settingUI(self):
        self.ui.table_log.setRowCount(0)  # 기존 내용을 지우기 위해 행 수를 0으로 설정
        for i, commandData in enumerate(self.commandDataList):
            row_position = self.ui.table_log.rowCount()
            self.ui.table_log.insertRow(row_position)

            # 각 셀에 데이터 삽입
            self.ui.table_log.setItem(row_position, 0, QTableWidgetItem(commandData["time"]))
            self.ui.table_log.setItem(row_position, 1, QTableWidgetItem(commandData["cmd_string"]))
            self.ui.table_log.setItem(row_position, 2, QTableWidgetItem(str(commandData["arg_string"])))
            self.ui.table_log.setItem(row_position, 3, QTableWidgetItem(str(commandData["is_finish"])))

    def update_sensing_table(self):
        self.ui.table_sensing.setRowCount(0)  # 기존 내용을 지우기 위해 행 수를 0으로 설정
        for i, data in enumerate(self.sensingDataList):
            row_position = self.ui.table_sensing.rowCount()
            self.ui.table_sensing.insertRow(row_position)

            # 테이블의 각 셀에 데이터 삽입
            self.ui.table_sensing.setItem(row_position, 0, QTableWidgetItem(data.get("time", "")))
            self.ui.table_sensing.setItem(row_position, 1, QTableWidgetItem(str(data.get("num1", ""))))
            self.ui.table_sensing.setItem(row_position, 2, QTableWidgetItem(str(data.get("num2", ""))))
            self.ui.table_sensing.setItem(row_position, 3, QTableWidgetItem(str(data.get("is_finish", ""))))
            self.ui.table_sensing.setItem(row_position, 4, QTableWidgetItem(data.get("manual_mode", "")))

    def go(self):
        self.commandData = self.makeCommandData("go", 100, 1)
        self.client.publish(commandTopic, json.dumps(self.commandData), qos=1)
        self.commandDataList.append(self.commandData)
        self.commandData = dict()
        self.settingUI()
        print(self.commandDataList)

    def mid(self):
        self.commandData = self.makeCommandData("mid", 100, 1)
        self.client.publish(commandTopic, json.dumps(self.commandData), qos=1)
        self.commandDataList.append(self.commandData)
        self.commandData = dict()
        self.settingUI()
        print(self.commandDataList)

    def back(self):
        self.commandData = self.makeCommandData("back", 100, 1)
        self.client.publish(commandTopic, json.dumps(self.commandData), qos=1)
        self.commandDataList.append(self.commandData)
        self.commandData = dict()
        self.settingUI()
        print(self.commandDataList)

    def left(self):
        self.commandData = self.makeCommandData("left", 100, 1)
        self.client.publish(commandTopic, json.dumps(self.commandData), qos=1)
        self.commandDataList.append(self.commandData)
        self.commandData = dict()
        self.settingUI()
        print(self.commandDataList)

    def right(self):
        self.commandData = self.makeCommandData("right", 100, 1)
        self.client.publish(commandTopic, json.dumps(self.commandData), qos=1)
        self.commandDataList.append(self.commandData)
        self.commandData = dict()
        self.settingUI()
        print(self.commandDataList)

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

    def arm_1(self, angle) :
        mapped_angle = angle
        command_data = self.makeCommandData("arm1", mapped_angle, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def arm_2(self, angle) :
        mapped_angle = angle
        command_data = self.makeCommandData("arm2", mapped_angle, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def closeEvent(self, event):
        self.commandData = self.makeCommandData("exit", 100, 1)
        self.client.publish(commandTopic, json.dumps(self.commandData), qos=1)

        self.commandDataList.append(self.commandData)
        self.commandData = dict()
        print(self.commandDataList)

        self.client.disconnect()

        current_time = datetime.now(korea_timezone)
        file_name = current_time.strftime("%Y-%m-%d") + ".txt"
        with open(file_name, "w") as file:
            for value in self.sensorData:
                file.write(str(value) + "\n")

        print("save data")
        event.accept()



    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            print("connected OK")
        else:
            print("Bad connection Returned code=", reason_code)

    # def on_message(self, client, userdata, msg):
    #     message = json.loads(msg.payload.decode("utf-8"))

    #     self.sensorData.append(message)
    #     self.sensingDataList = self.sensorData[-15:]
    #     self.update_sensing_table()


    # def on_message(self, client, userdata, msg):
    #     if msg.topic == cameraTopic:
    #         # 수신된 데이터 크기 출력 (디버깅용)
    #         print(f"Received image data size: {len(msg.payload)} bytes")

    #         # 이미지를 numpy 배열로 변환하고 디코딩
    #         jpg_as_np = np.frombuffer(msg.payload, dtype=np.uint8)
    #         frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)

    #         # 디코딩이 실패했을 경우 에러 메시지 출력
    #         if frame is None:
    #             print("Failed to decode the image. Check if the data format is correct.")
    #             return

    #         # 디코딩이 성공했을 경우 이미지 변환 및 QLabel에 표시
    #         rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         h, w, ch = rgb_image.shape
    #         bytes_per_line = ch * w
    #         qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    #         pixmap = QPixmap.fromImage(qt_image)

    #         # QLabel에 픽셀맵 설정
    #         self.ui.label_cam.setPixmap(pixmap.scaled(self.ui.label_cam.size()))
    #         self.ui.label_cam.setScaledContents(True)
    #     else:
    #         # 센서 데이터 처리
    #         data = json.loads(msg.payload.decode("utf-8"))
    #         self.sensorData.append(data)
    #         self.sensingDataList = self.sensorData[-15:]
    #         self.update_sensing_table()

    def on_message(self, client, userdata, msg):
        if msg.topic == cameraTopic:
            jpg_as_np = np.frombuffer(msg.payload, dtype=np.uint8)
            frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)

            if frame is not None:
                print("Received frame size:", frame.shape)  # 디버깅: 디코딩된 이미지 크기 확인
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qt_image)
                self.ui.label_cam.setPixmap(pixmap.scaled(self.ui.label_cam.size()))
                self.ui.label_cam.setScaledContents(True)
            else:
                print("Failed to decode the image")  # 디코딩 실패시 메시지 출력
        else:
            # 센서 데이터 처리
            data = json.loads(msg.payload.decode("utf-8"))
            self.sensorData.append(data)
            self.sensingDataList = self.sensorData[-15:]
            self.update_sensing_table()



    def closeEvent(self, event):
            self.client.disconnect()
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
