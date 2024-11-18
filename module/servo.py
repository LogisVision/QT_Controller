### servo.py

#import traitlets

from jetbot import Robot, Camera, bgr8_to_jpeg
from SCSCtrl import TTLServo
import threading
import cv2
import numpy as np
import paho.mqtt.client as mqtt
from datetime import datetime
import pytz
import time
import json
import random as rd

servoPos_1 = 0
servoPos_4 = 0
servoPos_5 = 0
xPos = 100
yPos = 0

robot = Robot()

# 서보 모터 ID
TURN_SERVO_ID = 1  # 좌우 서보
CAMERA_SERVO_ID = 2  # 상하 서보

# 각도 제한
TURN_MIN = -80
TURN_MAX = 80
CAMERA_MIN = -40
CAMERA_MAX = 25

# 현재 각도 저장
turn_angle = 0
camera_angle = 0

def adjust_motor(offset_x, offset_y):
    """
    offset_x와 offset_y 값을 기반으로 서보를 제어하여 카메라의 중심에 객체를 위치시킵니다.
    """
    global turn_angle, camera_angle

    # 좌우 모터 제어
    turn_angle += offset_x // 10  # 가중치 적용
    turn_angle = max(min(turn_angle, TURN_MAX), TURN_MIN)  # 각도 제한

    # 상하 모터 제어
    camera_angle += offset_y // 10  # 가중치 적용
    camera_angle = max(min(camera_angle, CAMERA_MAX), CAMERA_MIN)  # 각도 제한

    # 서보 모터 제어 명령
    servoAngleCtrl(TURN_SERVO_ID, turn_angle, 1, 150)  # 좌우 서보
    servoAngleCtrl(CAMERA_SERVO_ID, camera_angle, 1, 150)  # 상하 서보

    # 디버깅 출력
    print(f"Adjusted servo: turn_angle={turn_angle}, camera_angle={camera_angle}")


def limitCtl(maxInput, minInput, rawInput):
    if rawInput > maxInput:
        return maxInput
    elif rawInput < minInput:
        return minInput
    return rawInput

def camAngle(value):
    global servoPos_5
    servoPos_5 = limitCtl(25, -40, value)
    TTLServo.servoAngleCtrl(5, servoPos_5, 1, 150)

def turnAngle(value):
    global servoPos_1
    servoPos_1 = limitCtl(80, -80, value)
    TTLServo.servoAngleCtrl(1, servoPos_1, 1, 150)

def move_arms(value):
    x, y = map(int, value.split(","))
    x = max(85, min(x, 200))
    y = max(-50, min(y, 100))
    TTLServo.xyInput(x, y)
    
def grab(value):
    global servoPos_4
    servoPos_4 = value
    if servoPos_4 < -90:
        servoPos_4 = -90
    TTLServo.servoAngleCtrl(4, servoPos_4, 1, 150)

def arm_x(value):
    global xPos
    xPos = value
    if xPos < 85:
        xPos = 85
#     if xPos < -150 or xPos > 150:
#         pass
    #TTLServo.xyInput(xPos, yPos)
    TTLServo.servoAngleCtrl(2, value, 1, 150)

def arm_y(value):
    global yPos
    yPos = value
    if value <-50:
        value = -50

    #TTLServo.xyInput(xPos, yPos)
    TTLServo.servoAngleCtrl(3, value, 1, 150)
    
    
    
#차체 동작
def agv_stop():
    robot.stop()

def agv_forward():
    robot.forward(0.4)

def agv_backward():
    robot.backward(0.4)
    
def agv_right():
    robot.right(0.3)

def agv_left():
    robot.left(0.3)
    
    
class sensorReadPublish(threading.Thread):
    
    def __init__(self):
        super().__init__()
        self.th_flag = True
        
    def run(self):

        while self.th_flag:
		        #소수점 둘째자리까지 생성
            num1 = round(rd.random(),2)
            num2 = round(rd.random(),2)
            
            #Label widget 에 출력하기 위해 str 형변환
            num1lbl.value = str(num1)
            num2lbl.value = str(num2)
            
            #현재 시간 정보 가져오기
            current_time = datetime.now(korea_timezone)
            sensingData["time"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
            sensingData["num1"] = num1
            sensingData["num2"] = num2
            
            #GUI Controller 로 publish 하
            client.publish(sensingTopic, json.dumps(sensingData), 1)
            time.sleep(0.5)
        
    def stop(self):
        self.th_flag = False

        client = None
