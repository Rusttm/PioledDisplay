import cv2
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
# cap = cv2.VideoCapture("rtsp://192.168.1.80:8554/unicast", cv2.CAP_FFMPEG)
cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.11:554", cv2.CAP_FFMPEG)

ret, frame = cap.read()
print(f"{ret=}")
while ret:
    cv2.imshow('frame', frame)
    # do other processing on frame...

    ret, frame = cap.read()
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()