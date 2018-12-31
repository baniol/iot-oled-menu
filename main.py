#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def trigger_20(pin):
    print("20 ...\n")

def trigger_21(pin):
    print("21 ...\n")

def trigger_22(pin):
    print("22 ...\n")

def trigger_23(pin):
    print("23 ...\n")

def trigger_19(pin):
    print("19 ...\n")

GPIO.add_event_detect( 20, GPIO.FALLING, callback=trigger_20, bouncetime=300)
GPIO.add_event_detect( 21, GPIO.FALLING, callback=trigger_21, bouncetime=300)
GPIO.add_event_detect( 22, GPIO.FALLING, callback=trigger_22, bouncetime=300)
GPIO.add_event_detect( 23, GPIO.FALLING, callback=trigger_23, bouncetime=300)
GPIO.add_event_detect( 19, GPIO.FALLING, callback=trigger_19, bouncetime=300)


while True:
    pass
