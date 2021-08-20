import sys
# Write the effect here by defining a function with the same name as the file
import board
import neopixel
from time import sleep
def off(pwm_pin, num_pixels):
    # Pin possiblities
    pins = {
        '10': board.D10,
        '12': board.D12,
        '18': board.D18,
        '21': board.D21
    }
    NUM_PIXELS = int(num_pixels)
    BRIGHTNESS = 0.4
    OFF = (0,0,0)

    pixels = neopixel.NeoPixel(pins[str(pwm_pin)], NUM_PIXELS, brightness=1.0, auto_write=False)
    # auto_write False requires that pixels.show() be called to update the neopixels

    def strip_off():
        for i in range(NUM_PIXELS):
            pixels[i] = OFF
    strip_off()
    pixels.show()
# End effect code
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])