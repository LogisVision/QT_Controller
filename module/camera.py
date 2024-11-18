import cv2
import paho.mqtt.client as mqtt
import threading
import time

# MQTT 설정
broker_address = "70.12.225.174"
port = 1883
cameraTopic = "AGV/camera"

# MQTT 클라이언트 초기화 및 연결
client = mqtt.Client()
client.connect(broker_address, port)
client.loop_start()  # MQTT 클라이언트 백그라운드 실행

# GStreamer 파이프라인 초기화
gst_str = (
    "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, "
    "format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, "
    "format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
)
cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

# 종료 플래그 설정
stop_event = threading.Event()

# 카메라 프레임 송출 함수
def send_frame():
    try:
        while not stop_event.is_set() and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 프레임을 JPEG로 인코딩
            _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
            
            # MQTT로 이미지 전송
            jpg_as_text = buffer.tobytes()
            client.publish(cameraTopic, jpg_as_text)
    except Exception as e:
        print(f"Error in send_frame: {e}")
    finally:
        cap.release()
        client.disconnect()
        print("Camera and MQTT resources released.")

# 메인 스레드에서 send_frame을 실행하기 위한 설정
if __name__ == "__main__":
    try:
        # 해상도를 동적으로 설정할 수 있도록 사용자 입력 추가
        print("Enter desired resolution (width height), or press Enter for default (640x480):")
        user_input = input().strip()
        if user_input:
            try:
                width, height = map(int, user_input.split())
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
                print(f"Resolution set to: {width}x{height}")
            except ValueError:
                print("Invalid input. Using default resolution (640x480).")

        # 별도의 스레드에서 프레임 전송 실행
        frame_thread = threading.Thread(target=send_frame, daemon=True)
        frame_thread.start()

        while True:
            time.sleep(1)  # 메인 스레드 유지
    except KeyboardInterrupt:
        print("Exiting program...")
    finally:
        # 종료 플래그 설정 및 스레드 종료 대기
        stop_event.set()
        frame_thread.join()

        # 자원 해제
        if cap.isOpened():
            cap.release()
        client.loop_stop()
        client.disconnect()
        print("All resources released. Program terminated.")