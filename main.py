import cv2

from define import Define
from image_processing import ImageProcessor
from printer import Printer

webcam = cv2.VideoCapture(0)

imageProcessing = ImageProcessor()
printer = Printer()

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

    if key == ord('w'): # Quit
        break
    elif key == ord('e'): # Capture, Image process, Print
        #print("Captured Image Path:", Define.CAPTURED_IMG_PATH)
        imageProcessing.capture_image(ret, frame)
        imageProcessing.process_image()
        printer.print_image()
        
    
# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()