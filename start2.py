import board
import time
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageFont, ImageDraw

from digitalio import DigitalInOut, Direction
spi = busio.SPI(board.SCK, board.MOSI)

DC = DigitalInOut(board.D6)
CS = DigitalInOut(board.D5)
RST = DigitalInOut(board.D4)

disp = adafruit_ssd1306.SSD1306_SPI(128,64,spi, DC, RST, CS)
disp.fill(1)
disp.show()
time.sleep(2)
disp.fill(0)
disp.show()

#disp.begin()

# Clear display.
#disp.clear()
#disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
time.sleep(2)
disp.fill(0)
disp.show()

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
time.sleep(2)
disp.fill(0)
disp.show()

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Draw an ellipse.
draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
x += shape_width+padding
time.sleep(2)
disp.fill(0)
disp.show()


# Draw a rectangle.
draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
x += shape_width+padding
# Draw a triangle.
draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
x += shape_width+padding
# Draw an X.
draw.line((x, bottom, x+shape_width, top), fill=255)
draw.line((x, top, x+shape_width, bottom), fill=255)
x += shape_width+padding

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('Minecraftia.ttf', 8)

# Write two lines of text.
draw.text((x, top),    'Hello',  font=font, fill=255)
draw.text((x, top+20), 'World!', font=font, fill=255)

# Display image.
disp.image(image)
disp.display()
