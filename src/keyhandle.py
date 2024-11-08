import cv2
import time

from define import Define

class KeyHandler:
     _instance = None
     
     def __new__(cls):
          if cls._instance == None:
               cls._instance = super().__new__(cls)
          return cls._instance
     
     def __init__(self):
          if not hasattr(self, "_initialized"):
               self.last_pressed_time = {}
               self.debouce_delay = Define.DEBOUNCE_TIME
               self._initalized = True
          
     def is_key_pressed_once(self, key):
          key_code = ord(key)
          curr_time = time.time()
          
          if cv2.waitKey(1) == key_code:
               is_debounce_time_passed = key_code not in self.last_pressed_time or (curr_time - self.last_pressed_time[key_code] > self.debouce_delay)
               
               if is_debounce_time_passed:
                    self.last_pressed_time[key_code] = curr_time
                    return True
          else:
               self.last_pressed_time.pop(key_code, None)
          return False