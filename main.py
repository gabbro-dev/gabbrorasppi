import serial
import RPi.GPIO as GPIO
import time
#
from classes.led import Led
from classes.uart import UART
from classes.oled import oled

# Create objects
led = Led(17)
uart = UART(9600, "/dev/ttyV0")
oled = oled()

try:
    while True:
        command = uart.readComm()
        if command:
            print("Command recieved:", command)
            command = command.upper()

            # Led Commands
            if command == "ON":
                led.on()
            elif command == "OFF":
                led.off()
            elif command == "BLINK":
                led.blink()
            # Oled Display
            elif command == "SHOW":
                oled.displayText("Hello world!")
            elif command == "CLEAR":
                oled.clear()
            # Not a command
            else:
                print("Command not recognized")

except KeyboardInterrupt:
    print("End of the program")
    GPIO.cleanup()