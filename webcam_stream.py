import cv2

webcam = cv2.VideoCapture(0) 

while True:
    ret, frame = webcam.read()

    if not ret:
        print("Frame not received")
        break

    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()