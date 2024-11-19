import paho.mqtt.client as mqtt
import json
from servo import turnAngle, camAngle
import threading
import time

# MQTT 설정
broker_address = "70.12.225.174"
port = 1883
autoModeTopic = "AGV/auto_mode"

# 초기 서보 및 카메라 각도 설정
servo_angle = 0
camera_angle = 0

# 서보 및 카메라 각도 제한
TURN_MIN = -80
TURN_MAX = 80
CAMERA_MIN = -40
CAMERA_MAX = 25

# 오프셋 변수
offset_x = 0
offset_y = 0

# MQTT 클라이언트 초기화
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker in automode")
        client.subscribe(autoModeTopic)  # auto_mode 토픽 구독
    else:
        print("Connection failed with code", rc)

def on_message(client, userdata, msg):
    global offset_x, offset_y
    try:
        # MQTT 메시지에서 데이터 읽기
        data = json.loads(msg.payload.decode("utf-8"))
        offset_x = data.get("offset_x", 0)
        offset_y = data.get("offset_y", 0)
    except Exception as e:
        print("Error processing message:", e)

def process_tracking():
    """
    추적 알고리즘 실행: 오프셋을 기준으로 서보 및 카메라 각도를 조정
    """
    global servo_angle, camera_angle, offset_x, offset_y
    
    # 임계값 설정 (불필요한 조정 방지)
    threshold_x = 0
    threshold_y = 0
    
    # 좌우 (turnAngle) 조정
    if offset_x < -threshold_x:  # 화면 중심보다 왼쪽에 있을 때
        servo_angle -= 1
        if servo_angle < TURN_MIN:
            servo_angle = TURN_MIN
    elif offset_x > threshold_x:  # 화면 중심보다 오른쪽에 있을 때
        servo_angle += 1
        if servo_angle > TURN_MAX:
            servo_angle = TURN_MAX
    turnAngle(servo_angle)
    print(f"Turn angle adjusted to: {servo_angle}")

    # 상하 (camAngle) 조정
    if offset_y < -threshold_y:  # 화면 중심보다 위쪽에 있을 때
        camera_angle += 1
        if camera_angle > CAMERA_MAX:
            camera_angle = CAMERA_MAX
    elif offset_y > threshold_y:  # 화면 중심보다 아래쪽에 있을 때
        camera_angle -= 1
        if camera_angle < CAMERA_MIN:
            camera_angle = CAMERA_MIN
    camAngle(camera_angle)
    print(f"Camera angle adjusted to: {camera_angle}")

    # 다음 호출 예약
    threading.Timer(0.0, process_tracking).start()

# MQTT 설정
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)

# 3초 간격으로 추적 알고리즘 시작
threading.Timer(0.0, process_tracking).start()

client.loop_forever()