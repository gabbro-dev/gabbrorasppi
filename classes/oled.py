import time
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

class oled:
    def __init__(self, width = 128, height = 32, address = 0x3c):
        # Init i2C
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = SSD1306_I2C(width, height, self.i2c, addr=address)

        # Create empy image and object to draw
        self.image = Image.new("1", (width, height))
        self.draw = ImageDraw.Draw(self.image)
        # Load default font
        self.font = ImageFont.load_default()
        # Clean screen on init
        self.clear()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def displayText(self, text, x = 0, y = 0):
        # Clean image before drawing
        self.draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=0, fill=0)
        # Draw text in image
        self.draw.text((x, y), text, font=self.font, fill=255)
        # Pass image to Display
        self.oled.image(self.image)
        self.oled.show()