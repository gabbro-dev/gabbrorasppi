import serial

class UART:
    def __init__(self, baudrate, port, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout = timeout)
        self.ser.flush()

    def readComm(self):
        if self.ser.in_waiting > 0:
            command = self.ser.readline().decode("utf-8").strip()
            return command
        return None
    
    def close(self):
        self.ser.close()