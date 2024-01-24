# from https://www.tomshardware.com/how-to/diy-mouse-jiggler-raspberry-pi-pico with a few minor updates

import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

m = Mouse(usb_hid.devices)
button = DigitalInOut(board.BUTTON)
button.direction = Direction.INPUT
button.pull = Pull.UP
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

active = 0
button_press = 0
while True:
    # print(button.value)
    # print(active)
    if button.value == False and active == 0:
        active = 1
        button_press = 1
        print("Turning On")
        pixel.fill((32,32,32))
        sleep(5)
    elif button.value == True and active == 1 and button_press == 1:
        pixel.fill((0, 32, 0))

        # right
        m.move(100, 0, 0)
        # print("I'm so busy")
        sleep(0.5)       

        # down
        m.move(0, 100, 0)
        # print("I need a vacation")
        sleep(0.5)

        # left
        m.move(-100, 0, 0)
        # print("I'm working")
        sleep(0.5)
        
        # up
        m.move(0, -100, 0)
        # print("So much to do")
        sleep(0.5)
    elif button.value == False and active == 1 and button_press == 1:
        pixel.fill((32, 0, 0))
        active = 0
        button_press = 0
        print("Turning Off")
        sleep(5)    
    
    
