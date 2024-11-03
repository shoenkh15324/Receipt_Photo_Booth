import cv2

from define import Define
from image_processing import ImageProcessor

webcam = cv2.VideoCapture(0)
#cv2.namedWindow("Webcam", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("Webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

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
        ImageProcessor().capture_image(ret, frame)
        ImageProcessor().process_image()
        ImageProcessor().show_image_to_print()
        
# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()