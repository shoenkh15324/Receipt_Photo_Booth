import time

from define import Define
from serial_communication import SerialCommunicator

class Button():
     def __init__(self, serial_comm, debounce_time = Define.BUTTON_DEBOUNCE_TIME):
          self.serial_comm = SerialCommunicator()
          self.debounce_time = debounce_time # sec
          self.last_pressed_time = 0
     
     def debounce_button(self):
          current_time = time.time()
          data = self.serial_comm.read_data()
          
          if data:
               if (current_time - self.last_pressed_time) > self.debounce_time:
                    self.last_pressed_time = current_time
                    return data
          return None
