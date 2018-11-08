#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.add_event_detect( 20, GPIO.FALLING, callback=trigger_1, bouncetime=300)

def trigger_1():
    print("20 ...\n")

while True:
    time.sleep(5)
    print("sleeping ...")
