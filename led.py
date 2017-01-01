import sys
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # we want to reference the GPIO by chip number
GPIO.setwarnings(False)

# LED colors pins
redPin = 17
greenPin = 27
bluePin = 22

def ledOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def ledOff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def redOn():
    ledOn(redPin)

def greenOn():
    ledOn(greenPin)

def blueOn():
    ledOn(bluePin)


GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)

ledOn(redPin)
sleep(2)
ledOff(redPin)
sleep(1)
ledOn(greenPin)
sleep(2)
ledOff(greenPin)
sleep(1)
ledOn(bluePin)
sleep(2)
ledOff(bluePin)
sleep(1)

