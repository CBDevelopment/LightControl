import sys
import os
# Write the effect here by defining a function with the same name as the file
import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import random
from random import randint
import threading
from time import sleep

def stars_effect_string(pwm_pin, num_pixels):
    # Pin possiblities
    pins = {
        '10': board.D10,
        '12': board.D12,
        '18': board.D18,
        '21': board.D21
    }
    # Log the PID of this process to the logs folder in effects
    pid = os.getpid()
    with open(f'logs/OpenEffect{pwm_pin}.txt', 'a') as f:
        f.write(str(pid))

    # Star flashing program

    # To Do:
    # Run all LEDs from a single power supply? More powerful supply (more amps?)
    # Calculate power draw for all strips in parallel with supply
    NUM_PIXELS = int(num_pixels)
    BRIGHTNESS = 0.4

    YELLOW = fancy.CRGB(255,255,0)
    BLUE = fancy.CRGB(255,140,255)
    # BLUE = fancy.CRGB(140,355,255)
    BLACK = fancy.CRGB(0,0,0)
    OFF = (0,0,0)

    pixels = neopixel.NeoPixel(pins[str(pwm_pin)], NUM_PIXELS, brightness=1.0, auto_write=False)
    # auto_write False requires that pixels.show() be called to update the neopixels

    def strip_off():
        for i in range(NUM_PIXELS):
            pixels[i] = OFF
    strip_off()
    pixels.show()

    def pick_pixels(num_pixels):
        picked_pixels = []
        for i in range(num_pixels):
            picked = True
            while picked:
                pixel_index = randint(0, NUM_PIXELS - 1)
                if pixel_index in picked_pixels:
                    continue
                else:
                    picked_pixels.append(pixel_index)
                    picked = False
        return picked_pixels   

    def fade(pixel_index, color):
        # Start the pixel in the off state
        pixels[pixel_index] = OFF

        gradient = fancy.expand_gradient([
            (0.0, BLACK),
            (0.5, color),
            (1.0, BLACK)
        ], 20)

        index = 0

        for i in range(20):
            color = gradient[index]
            adjusted = fancy.gamma_adjust(color, brightness=BRIGHTNESS)
            pixels[pixel_index] = adjusted.pack()
            pixels.write()

            index += 1
            if index > len(gradient)-1:
                index = 0
            sleep(0.05)
            
        

    def stars(num_pixels):
        pixels_to_fade = pick_pixels(num_pixels)
        for i in range(len(pixels_to_fade)):
            thread = threading.Thread(target=fade, args=(pixels_to_fade[i], [YELLOW, BLUE][randint(0,1)]))
            thread.daemon = True
            thread.start()
            

    for i in range(100):
        num_stars = randint(0,10)
        stars(num_stars)
        sleep(random.uniform(0.5,2.0))
# End effect code
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])