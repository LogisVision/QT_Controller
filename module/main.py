### main.py
import paho.mqtt.client as mqtt
import json
import threading
import subprocess
from servo import *
from camera import send_frame

broker_address = "70.12.225.174"
port = 1883
commandTopic = "AGV/command"
controlTopic = "AGV/control"

client = mqtt.Client()
client.connect(broker_address, port)

# Auto Mode 상태
auto_mode_active = False
automode_process = None

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
        TTLServo.servoAngleCtrl(1, 0, 1, 150)
        TTLServo.servoAngleCtrl(2, 0, 1, 150)
        TTLServo.servoAngleCtrl(3, 0, 1, 150)
        TTLServo.servoAngleCtrl(4, 0, 1, 150)
        TTLServo.servoAngleCtrl(5, 0, 1, 150)
        print("Servo Initialized")
    else:
        print("Bad connection Returned code=", rc)

def on_message(client, userdata, msg):
    global auto_mode_active, automode_process
    if msg.topic == controlTopic:
        command = msg.payload.decode("utf-8")
        if command == "AUTO_ON":
            auto_mode_active = True
            if automode_process is None:
                automode_process = subprocess.Popen(["python3", "automode.py"])
            print("Auto mode process started.")
        elif command == "AUTO_OFF":
            auto_mode_active = False
            if automode_process:
                automode_process.terminate()
                automode_process = None
            print("Auto mode process stopped.")
    elif msg.topic == commandTopic and not auto_mode_active:
        handle_manual_commands(msg.payload.decode("utf-8"))

def handle_manual_commands(payload):
    try:
        message = json.loads(payload)
        command = message.get("cmd_string", "")
        arg = message.get("arg_string", 0)

        if isinstance(arg, str) and ',' in arg:
            x, y = map(int, arg.split(','))
        else:
            arg = int(float(arg)) if isinstance(arg, str) and '.' in arg else int(arg)

        if command == "go":
            agv_forward()
        elif command == "back":
            agv_backward()
        elif command == "mid":
            agv_stop()
        elif command == "left":
            agv_left()
        elif command == "right":
            agv_right()
        elif command == "grab_angle":
            grab(int(arg))
        elif command == "camera_angle":
            camAngle(int(arg))
        elif command == "camera_turn_angle":
            turnAngle(int(arg))
        elif command == "move_arms":
            move_arms(f"{x},{y}")
        elif command == "arm_x":
            arm_x(int(arg))
        elif command == "arm_y":
            arm_y(int(arg))
        elif command == "reset":
            reset_servos()
    except Exception as e:
        print("Error processing manual command:", e)

def reset_servos():
    for i in range(1, 6):
        TTLServo.servoAngleCtrl(i, 0, 1, 150)
    print("Servos reset.")

client.on_connect = on_connect
client.on_message = on_message

client.loop_start()

camera_thread = threading.Thread(target=send_frame, daemon=True)
camera_thread.start()

client.subscribe(commandTopic, 1)
client.subscribe(controlTopic, 1)

try:
    while True:
        pass
except KeyboardInterrupt:
    if automode_process:
        automode_process.terminate()
    client.disconnect()