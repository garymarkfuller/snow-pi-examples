from microbit import *
import neopixel
from random import randint

# Setup the SnowPi on pin2 with a length of 12 pixels
np = neopixel.NeoPixel(pin2, 12)

while True:
    for np_col in range(0, 4):
        if(np_col == 0):
            red = 60
            green = 0
            blue = 0
        if(np_col == 1):
            red = 0
            green = 60
            blue = 0
        if(np_col == 2): 
            red = 0
            green = 0
            blue = 60
        if(np_col == 3):
            red = 60
            green = 60
            blue = 60
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (red, green, blue)
            np.show()
            sleep(50) 
        for np_flash in range(0, 10): 
            np.clear()
            sleep(100)
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (red, green, blue)
            np.show()
            sleep(100)            
        sleep(1000)

