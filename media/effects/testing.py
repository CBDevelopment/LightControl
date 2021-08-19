import sys
# Write the effect here by defining a function with the same name as the file
def testing(pwm_pin, num_pixels):
    for i in range(10):
        print("Hello there")

    print("Made it here")
# End effect code
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])