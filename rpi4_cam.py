
import cv2
# import picamera2
cap = cv2.VideoCapture(0)

#Configure output video compression, format, frame rate, frame size
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = 'qvideo.avi'  # Output video file name
frame_rate = 30.0  # Number of frames per second
frame_size = (640, 480)  # Frame size (width, height)

#Instantiate video writer object
video_writer = cv2.VideoWriter(output_file, fourcc, frame_rate, frame_size)

while True:

    result, frame = cap.read()
    # print(result, frame)
    cv2.imshow("PI Camera", frame)
    video_writer.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
video_writer.release()
cv2.destroyAllWindows()
