import paho.mqtt.client as mqtt
import json
from servo import turnAngle, camAngle

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

# MQTT 클라이언트 초기화
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker in automode")
        client.subscribe(autoModeTopic)  # auto_mode 토픽 구독
    else:
        print("Connection failed with code", rc)

def on_message(client, userdata, msg):
    try:
        # MQTT 메시지에서 데이터 읽기
        data = json.loads(msg.payload.decode("utf-8"))
        offset_x = data.get("offset_x", 0)
        offset_y = data.get("offset_y", 0)
        process_tracking(offset_x, offset_y)
    except Exception as e:
        print("Error processing message:", e)

def process_tracking(offset_x, offset_y):
    """
    추적 알고리즘 실행: 오프셋을 기준으로 서보 및 카메라 각도를 조정
    """
    global servo_angle, camera_angle

    # 좌우 (turnAngle) 조정
    if offset_x != 0:
        servo_angle += offset_x // 10
        servo_angle = max(min(servo_angle, TURN_MAX), TURN_MIN)  # 제한 범위 내로 조정
        turnAngle(servo_angle)  # 서보 모터 제어
        print(f"Turn angle adjusted to: {servo_angle}")

    # 상하 (camAngle) 조정
    if offset_y != 0:
        camera_angle += offset_y // 10
        camera_angle = max(min(camera_angle, CAMERA_MAX), CAMERA_MIN)  # 제한 범위 내로 조정
        camAngle(camera_angle)  # 카메라 서보 제어
        print(f"Camera angle adjusted to: {camera_angle}")

# MQTT 설정
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_forever()