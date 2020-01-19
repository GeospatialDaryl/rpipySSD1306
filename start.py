
import board
import time
import busio
import digitalio
import adafruit_ssd1306


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

