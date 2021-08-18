import sys
# Write the effect here by defining a function with the same name as the file
import threading

def neopixels(pwm_pin,num_pixels):
    def printing():
        print("Hello")

    for i in range(10):
        thread = threading.Thread(target=printing)
        thread.start()
# End effect code
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])