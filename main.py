import serial
import RPi.GPIO as GPIO
import time
#
from classes.led import Led
from classes.uart import UART

# Create objects
led = Led(2)
uart = UART(9600, "/dev/ttyV0")

try:
    while True:
        command = uart.readComm()
        if command:
            print("Command recieved:", command)
            command = command.upper()

            if command == "ON":
                led.on()
            elif command == "OFF":
                led.off()
            elif command == "BLINK":
                led.blink()
            else:
                print("Command not recognized")

except KeyboardInterrupt:
    print("End of the program")
    GPIO.cleanup()