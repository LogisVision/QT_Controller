

from jetbot import Robot
from SCSCtrl import TTLServo
import threading
import json
from datetime import datetime
import pytz
import time
import random as rd

# 서보 모터 ID 및 초기값 설정
servoPos_1 = 0
servoPos_4 = 0
servoPos_5 = 0
xPos = 100
yPos = 0

robot = Robot()

TURN_SERVO_ID = 1  # 좌우 서보
CAMERA_SERVO_ID = 2  # 상하 서보

TURN_MIN = -80
TURN_MAX = 80
CAMERA_MIN = -40
CAMERA_MAX = 25

turn_angle = 0
camera_angle = 0



# 제한 함수
def limitCtl(maxInput, minInput, rawInput):
    return max(min(rawInput, maxInput), minInput)

# 서보 동작 함수
def camAngle(value):
    global servoPos_5
    servoPos_5 = limitCtl(25, -40, value)
    TTLServo.servoAngleCtrl(5, servoPos_5, 1, 100)

def turnAngle(value):
    global servoPos_1
    servoPos_1 = limitCtl(80, -80, value)
    TTLServo.servoAngleCtrl(1, servoPos_1, 1, 100)

def move_arms(value):
    x, y = map(int, value.split(","))
    x = max(85, min(x, 200))
    y = max(-50, min(y, 100))
    TTLServo.xyInput(x, y)

def grab(value):
    global servoPos_4
    servoPos_4 = limitCtl(-90, 90, value)
    TTLServo.servoAngleCtrl(4, servoPos_4, 1, 150)

def arm_x(value):
    global xPos
    xPos = limitCtl(85, 200, value)
    TTLServo.servoAngleCtrl(2, xPos, 1, 150)

def arm_y(value):
    global yPos
    yPos = limitCtl(-50, 100, value)
    TTLServo.servoAngleCtrl(3, yPos, 1, 150)

# 이동 관련 동작
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

# 자동 제어용 서보 조정
def adjust_motor(offset_x, offset_y):
    global turn_angle, camera_angle

    turn_angle += offset_x // 10  # 좌우 모터 조정
    turn_angle = limitCtl(TURN_MAX, TURN_MIN, turn_angle)

    camera_angle += offset_y // 10  # 상하 모터 조정
    camera_angle = limitCtl(CAMERA_MAX, CAMERA_MIN, camera_angle)

    TTLServo.servoAngleCtrl(TURN_SERVO_ID, turn_angle, 1, 150)  # 좌우 서보 제어
    TTLServo.servoAngleCtrl(CAMERA_SERVO_ID, camera_angle, 1, 150)  # 상하 서보 제어

    print(f"Adjusted Motor: turn_angle={turn_angle}, camera_angle={camera_angle}")

# 수동 제어
def handle_manual_commands(payload):
    global turn_angle, camera_angle
    try:
        message = json.loads(payload)
        command = message.get("cmd_string", "")
        arg = message.get("arg_string", 0)

        if command == "go":
            agv_forward()
        elif command == "back":
            agv_backward()
        elif command == "left":
            agv_left()
        elif command == "right":
            agv_right()
        elif command == "mid":
            agv_stop()
        elif command == "camera_angle":
            angle = int(arg)
            camera_angle = limitCtl(CAMERA_MAX, CAMERA_MIN, angle)
            TTLServo.servoAngleCtrl(CAMERA_SERVO_ID, camera_angle, 1, 150)
        elif command == "camera_turn_angle":
            angle = int(arg)
            turn_angle = limitCtl(TURN_MAX, TURN_MIN, angle)
            TTLServo.servoAngleCtrl(TURN_SERVO_ID, turn_angle, 1, 150)
        elif command == "reset":
            reset_servos()
        elif command == "move_arms":
            move_arms(arg)
        elif command == "grab_angle":
            grab(int(arg))
        elif command == "arm_x":
            arm_x(int(arg))
        elif command == "arm_y":
            arm_y(int(arg))
    except Exception as e:
        print("Error in handle_manual_commands:", e)

# 서보 초기화
def reset_servos():
    for i in range(1, 6):
        TTLServo.servoAngleCtrl(i, 0, 1, 150)
    print("Servos reset.")

# 센서 데이터 읽기 및 발행
class sensorReadPublish(threading.Thread):
    def __init__(self):
        super().__init__()
        self.th_flag = True

    def run(self):
        while self.th_flag:
            num1 = round(rd.random(), 2)
            num2 = round(rd.random(), 2)

            # 현재 시간 정보 가져오기
            current_time = datetime.now(pytz.timezone("Asia/Seoul"))
            sensingData = {
                "time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                "num1": num1,
                "num2": num2,
            }

            # 데이터 전송 (수정 필요시 MQTT 클라이언트 추가 가능)
            print(f"Published Sensor Data: {sensingData}")
            time.sleep(0.5)

    def stop(self):
        self.th_flag = False