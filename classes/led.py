import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print("Led ON")

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        print("Led OFF")

    def blink(self, delay = 0.5):
        self.on()
        time.sleep(delay)
        self.off()
        time.sleep(delay)
        self.on()
        time.sleep(delay)
        self.off()
        time.sleep(delay)