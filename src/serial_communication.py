import serial
import serial.tools.list_ports

from define import Define

class SerialCommunicator:
     _instance = None
     
     def __new__(cls, *args, **kwargs):
          if cls._instance == None:
               cls._instance = super().__new__(cls)
          return cls._instance
     
     def __init__(self,
                  port = None,
                  baudrate = Define.SERIAL_COMM_BAUDRATE,
                  timeout = Define.SERIAL_COMM_TIMEOUT):
          if not hasattr(self, '_initialized'):
               self.port = port
               self.baudrate = baudrate
               self.timeout = timeout
               self.serial_connection = None
               self._initalized = True
          
     # Find and Connect arduino     
     def find_arduino_port(self):
          ports = serial.tools.list_ports.comports()
          
          for port, desc, _ in sorted(ports):
               if "Arduino" in desc:
                    self.port = port
                    print(f"Find arduino port: {self.port}")
                    return self.port
          
          print("No arduino port")
          return None
     
     # Open and Connect serial port
     def connect(self):
          self.find_arduino_port()
          
          if self.port is None:
               raise ValueError("You must connect by specifying a port or via auto-detection.")
          
          try:
               self.serial_connection = serial.Serial(self.port, 
                                                      self.baudrate, 
                                                      timeout=self.timeout)
               print(f"Connect port: {self.port}")
          except serial.SerialException as e:
               print(f"[Error]: {e}")
               self.serial_connection = None
               
     def disconnect(self):
          if self.serial_connection and self.serial_connection.is_open:
               self.serial_connection.close()
               print("Disconnect.")
               
     def read_data(self):
          if self.serial_connection and self.serial_connection.is_open:
               data = self.serial_connection.readline().decode().strip()
               return data
          else:
               return None
          
     def write_data(self, data):
          if self.serial_connection and self.serial_connection.is_open:
               self.serial_connection.write(data.encode())
               print(f"Send data: {data}")