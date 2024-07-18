
import cv2
# import picamera2
cap = cv2.VideoCapture(0)
while True:

    result, frame = cap.read()
    # print(result, frame)
    cv2.imshow("PI Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()