
import board
import time
import busio
import digitalio
import adafruit_ssd1306
import gaugette.rotary_encoder
import gaugette.switch
import gaugette.gpio
import time

import classMixer_v1

from digitalio import DigitalInOut, Direction

# set up SPI
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

# objMixr

mixr = classMixer_v1.Mixer(disp)
mixr._update_rects()
mixr._write_screen()

#  Config IO Wardware

A_PIN  = 0
B_PIN  = 1
SW_PIN = 2

gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(gpio, A_PIN, B_PIN)
encoder.start()
switch = gaugette.switch.Switch(gpio, SW_PIN)
last_state = None

while True:
    delta = encoder.get_steps()
    if delta!=0:
        print ("rotate %d" % delta)
    else:
        time.sleep(0.05)

    sw_state = switch.get_state()
    if sw_state != last_state:
        print ("switch %d" % sw_state)
        mixr._set_SelectedBar()
        last_state = sw_state


