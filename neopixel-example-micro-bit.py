"""
    neopixel-example-micro-bit.py

    Repeatedly displays random colours onto the SnowPI.
    This example requires a SnowPi attached to a Micro:Bit and was created using MicroPython and the Mu editor.
    MicroPython can be found at https://github.com/micropython/micropython, and this example is a modified version of code found on https://docs.micropython.org/en/latest/

"""
from microbit import *
import neopixel
from random import randint

# Setup the SnowPi on pin2 with a length of 12 pixels
np = neopixel.NeoPixel(pin2, 12)

while True:
    #Iterate over each LED on the SnowPi

    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip (not really needed for this example, but I left it in from the original code)
        np.show()
        sleep(100)
