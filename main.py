import cv2
import define
from image_processing import ImageProcessing

webcam = cv2.VideoCapture(0)

imageProcessing = ImageProcessing()

if not webcam.isOpened():
    print("Error: Webcam Open Failed")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = webcam.read()
    key = cv2.waitKey(1)

    if not ret:
        print("Error: Could not read frame")
        exit()

    frame = cv2.flip(frame, 1)

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Break the loop on pressing 'w'
    if key == ord('w'):
        break
    # Screenshot
    elif key == ord('e'):
        imageProcessing.capture(ret, frame)
        imageProcessing.convertCapturedImageToPrinterImg()
        
        

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()