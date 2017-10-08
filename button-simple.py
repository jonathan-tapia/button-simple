import RPi.GPIO as GPIO
import time

button = 6 # define button pin location
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Button waiting
while True:
    input_state = GPIO.input(button)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)