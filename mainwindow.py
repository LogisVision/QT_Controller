
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
from PySide6.QtCore import QTimer, QUrl, QPoint

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

    # 얼굴의 실제 너비(cm)
    KNOWN_WIDTH = 14.0
    # 카메라의 초점 거리(픽셀 단위)
    FOCAL_LENGTH = 389.12
    servo_angle = 0
    cam_angle = -7
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

        self.ui.label_touch.setMouseTracking(True)
        self.ui.label_touch.mouseMoveEvent = self.update_mouse_position

        #디버깅용 내장 카메라 코드
        #self.cap = cv2.VideoCapture(0)  # Set to default camera
        #self.timer = QTimer()
        #self.timer.timeout.connect(self.update_frame)
        #self.timer.start(30)  # Update every 30 ms
        #여기까지 카메라 코드
        # Load cascade file for face detection
        self.face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')#cascade 모델


        # btn_grab 클릭 시 move_arms 함수가 호출되도록 설정
        self.ui.btn_grab.clicked.connect(self.on_grab_clicked)

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


    def on_grab_clicked(self):
        # btn_grab 클릭 시 특정 x, y 좌표로 move_arms 호출
        x = 100  # 원하는 x 좌표
        y = 50   # 원하는 y 좌표
        self.move_arms(y)


    def init(self):
        print("init")

    def load_url(self, url):
        self.web_view.setUrl(QUrl(url))

    def update_mouse_position(self, event):
        # label_cam의 크기 가져오기
        widget_width = self.ui.label_touch.width()
        widget_height = self.ui.label_touch.height()

        # 마우스의 절대 좌표를 중심 기준 좌표로 변환
        x = int(event.position().x() - widget_width / 2)
        y = int(event.position().y() - widget_height / 2)

        # Print debug info to confirm the coordinates
        print(f"Mouse position: x={x}, y={y}")

        # x 좌표를 이용해 회전 각도를 계산하여 rotate_arms 호출
        angle = self.calculate_rotate_angle(x, widget_width)
        self.rotate_arms(angle)

        # y 좌표를 활용하여 팔 이동
        self.move_arms(y)


        # 중심을 기준으로 변환된 좌표를 UI에 표시
        self.ui.label_mouse_x.setText("X: "+str(x))
        self.ui.label_mouse_y.setText(str(y))

    def calculate_rotate_angle(self, x, widget_width):
        """
        중심을 기준으로 변환된 x 좌표를 회전 각도로 변환하는 함수
        x: 중심 기준으로 변환된 마우스 x 좌표
        widget_width: label_cam의 전체 너비
        """
        # 회전 각도의 범위 설정
        max_angle = 80
        min_angle = -80

        # x 좌표를 -80 ~ 80 사이로 매핑
        angle = int((x / (widget_width / 2)) * (max_angle - min_angle) / 2)
        return angle


    def send_xy_set(self, x, y):
        pass

    def start(self):
        # MQTT 클라이언트 생성
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        # 연결 시 콜백 함수 설정
        self.client.on_connect = self.on_connect
        # 메시지 수신 시 콜백 함수 설정
        self.client.on_message =  self.on_message

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

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3,3)

        # Draw bounding box around each detected face
        #for (x, y, w, h) in faces:
            # Draw rectangle around face
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Calculate the center of the bounding box
            #center_x, center_y = x + w // 2, y + h // 2
            # Draw a small square at the center of the bounding box
            #cv2.rectangle(frame, (center_x - 15, center_y - 15), (center_x + 15, center_y + 15), (0, 255, 0), 2)

            # Display coordinates in line_x and line_y
            #self.ui.line_mouse_x.setText(str(center_x))
            #self.ui.line_mouse_y.setText(str(center_y))

            # 얼굴과의 거리 계산 (센티미터 단위)
            #distance_cm = (self.KNOWN_WIDTH * self.FOCAL_LENGTH) / w
            #self.ui.label_distance.setText(f"{distance_cm:.2f} cm")  # label_distance에 표시

            # Convert to RGB for display in QLabel
        #내장 캠 관련 처리 코드
        #rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #h, w, ch = rgb_image.shape
        #bytes_per_line = ch * w
        #qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # Update QLabel with the new frame
        #pixmap = QPixmap.fromImage(qt_image)
        #self.ui.label_cam.setPixmap(pixmap.scaled(self.ui.label_cam.size()))


        """
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
        """

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



    def mode_auto(self):
        # AUTO 버튼이 활성화되면 MANUAL 버튼 비활성화
        if self.ui.btn_auto.isChecked():
            self.ui.btn_manual.setChecked(False)

    def mode_manual(self):
        # MANUAL 버튼이 활성화되면 AUTO 버튼 비활성화
        if self.ui.btn_manual.isChecked():
            self.ui.btn_auto.setChecked(False)

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

    def move_arms(self,y) :
        # `x`, `y` 좌표로 명령 데이터를 생성하고 MQTT로 전송
        #xy_values = f"{x},{y}"
        command_data = self.makeCommandData("move_arms", y, 1)
        # MQTT 토픽으로 좌표 데이터를 JSON 형식으로 전송
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        # 명령 데이터 저장 및 UI 업데이트
        self.commandDataList.append(command_data)
        self.settingUI()




    # 얼굴 중심에 따라 서보 모터를 회전시키는 함수

    def auto_rotate(self, face_center_x, face_center_y, widget_width, widget_height):
        # Calculate the center x and y coordinates of label_cam
        screen_center_x = widget_width // 2
        screen_center_y = widget_height // 2

        # Calculate the horizontal and vertical offsets from the center
        offset_x = face_center_x - screen_center_x
        offset_y = face_center_y - screen_center_y

        # Set thresholds to avoid unnecessary adjustments when close to the center
        threshold_x = 1
        threshold_y = 1


        # Horizontal adjustment (left/right rotation) using servo_angle
        if offset_x < -threshold_x:
            self.servo_angle -= 1
            if self.servo_angle < -80:  # Lower limit for horizontal servo angle
                self.servo_angle = -80
        elif offset_x > threshold_x:
            self.servo_angle += 1
            if self.servo_angle > 80:  # Upper limit for horizontal servo angle
                self.servo_angle = 80

        """
        if offset_y < -threshold_y:
            self.cam_angle +=1
            if self.cam_angle > 25 :
                self.cam_angle = 25
        elif offset_y > threshold_y:
            self.cam_angle -=1
            if self.cam_angle < -40:
                self.cam_angle = -40
        """

        # Apply the calculated angles to the servo motor for horizontal alignment
        # and to the camera for vertical alignment
        self.rotate_arms(self.servo_angle)
        #self.camera_angle(self.cam_angle)






    def rotate_arms(self, angle):
        command_data = self.makeCommandData("rotate_arms", angle, 1)
        self.client.publish(commandTopic, json.dumps(command_data), qos=1)
        self.commandDataList.append(command_data)
        self.settingUI()

    def set_reset(self):
        command_data = self.makeCommandData("reset", 0, 1)
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



    # mqtt 카메라 영상 수신 및 처리
    """
    def on_message(self, client, userdata, msg):
        if msg.topic == cameraTopic:
            jpg_as_np = np.frombuffer(msg.payload, dtype=np.uint8)
            frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)

            if frame is not None:
                print("Received frame size:", frame.shape)  # 디버깅: 디코딩된 이미지 크기 확인
                gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray_image, 1.3,3)

                # Bounding box 그리기
                for (x,y,w,h) in faces :
                    #얼굴 주변 박스
                    cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),3)

                    # 박스 중심 계산
                    center_x, center_y = x+w //2, y+h//2
                    # 작은 중심박스
                    cv2.rectangle(frame, (center_x - 15, center_y - 15), (center_x + 15, center_y + 15), (0, 255, 0), 2)

                    # Calculate distance in centimeters (assuming face width in cm and focal length are known)
                    distance_cm = (self.KNOWN_WIDTH * self.FOCAL_LENGTH) / w
                    self.ui.label_distance.setText(f"{distance_cm:.2f} cm")



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
    """


    def on_message(self, client, userdata, msg):
        try:
            if msg.topic == cameraTopic:
                jpg_as_np = np.frombuffer(msg.payload, dtype=np.uint8)
                frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)

                if frame is not None:
                    print("Received frame size:", frame.shape)  # 디버깅: 디코딩된 이미지 크기 확인

                    # 그레이스케일 변환 및 얼굴 검출
                    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = self.face_cascade.detectMultiScale(gray_image, 1.3, 3)

                    # 첫 번째 얼굴에 대해서만 처리
                    if len(faces) > 0:
                        x, y, w, h = faces[0]  # 첫 번째 얼굴 선택

                        # 얼굴 주위에 파란 사각형 그리기
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # 박스 중심 계산 및 중심에 작은 녹색 사각형 그리기
                        center_x = x + w // 2
                        center_y = y + w // 2
                        cv2.rectangle(frame, (center_x - 8, y + h // 2 - 8), (center_x + 8, y + h // 2 + 8), (0, 255, 0), 2)

                        # 모터 회전을 위한 x축 오프셋 계산
                        self.auto_rotate(center_x,center_y, self.ui.label_cam.width(),self.ui.label_cam.height())

                        #self.auto_rotate(center_x, center_y, self.ui.label_cam.width(), self.ui.label_cam.height())

                        # 거리 계산
                        distance_cm = (self.KNOWN_WIDTH * self.FOCAL_LENGTH) / w
                        cv2.putText(
                            frame,
                            f"{distance_cm:.2f} cm",
                            (x, y - 10),  # 텍스트 위치 (얼굴 상단 바로 위)
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.0,  # 텍스트 크기
                            (0, 255, 0),  # 텍스트 색상 (녹색)
                            2,  # 텍스트 두께
                            cv2.LINE_AA,
                        )

                    # Qt에 맞게 이미지 변환
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qt_image)
                    self.ui.label_cam.setPixmap(pixmap.scaled(self.ui.label_cam.size()))
                else:
                    print("Failed to decode the image")
            else:
                try:
                    data = json.loads(msg.payload.decode("utf-8"))
                    self.sensorData.append(data)
                    self.sensingDataList = self.sensorData[-15:]
                    self.update_sensing_table()
                except json.JSONDecodeError as e:
                    print("JSON decoding error:", e)

        except Exception as e:
            print("Error in on_message:", e)






    def closeEvent(self, event):
            self.client.disconnect()
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
