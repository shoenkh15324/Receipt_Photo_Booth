import cv2
import os

from define import Define
from image_processing import ImageProcessor
from serial_communication import SerialCommunicator
from button import Button

def check_image_file_exist():
    if not os.path.exists(os.path.dirname(Define.IMAGE_FOLDER_DIR)):
        os.makedirs(Define.IMAGE_FOLDER_DIR)

def init():
    serial_comm = SerialCommunicator()
    
    check_image_file_exist()
    serial_comm.connect()
    
def main():
    serial_comm = SerialCommunicator()
    
    webcam = cv2.VideoCapture(0)
    #cv2.namedWindow("Webcam", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("Webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    if not webcam.isOpened():
        print("Error: Webcam Open Failed")
        exit()

    while True:
        # Capture frame-by-frame
        ret, frame = webcam.read()
        
        button = Button.debounce_button()
        keybaord = cv2.waitKey(1)

        if not ret:
            print("Error: Could not read frame")
            exit()

        # Vertical invert
        frame = cv2.flip(frame, 1)

        # Display the resulting frame
        cv2.imshow('Webcam', frame)

        if keybaord == ord('q'): # Quit
            break
        
        if button == 'W': # Capture, Image process, Print
            ImageProcessor().capture_image(ret, frame)
            ImageProcessor().process_image()
            ImageProcessor().show_image_to_print()
            
    # Release the webcam and close all OpenCV windows
    webcam.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    init()
    main()