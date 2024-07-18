
import cv2
# import picamera2
cap = cv2.VideoCapture(0)
result, frame = cap.read()
print(result, frame)
