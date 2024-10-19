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
                print("Showing text in Oled")
                oled.displayText("Hello world!")
            elif command == "CLEAR":
                print("Oled cleared")
                oled.clear()
            elif command == "DISPLAY":
                print("Input the text to display")
                while True:
                    command = uart.readComm()
                    if command:
                        if command.upper() == "X":
                            break
                        else:
                            oled.displayText(command)
                            print("Text displayed:", command)
                            break
            # Not a command
            else:
                print("Command not recognized:", command)

except KeyboardInterrupt:
    print("End of the program")
    GPIO.cleanup()