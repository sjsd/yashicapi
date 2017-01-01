from time import sleep
from datetime import datetime
from picamera import PiCamera
from subprocess import call
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # we want to reference the GPIO by chip number
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # shutter is connected to pin 18
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) # upload images is connected to pin 15

GPIO.setwarnings(False) # Turn off warings

# LED colors pins. Note, this is by the BCM-setup
redPin = 17
greenPin = 27
bluePin = 22


REMOTE_SERVER = "www.dropbox.com"

def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        print("Is connected to internet")
        return True
    except:
        pass
    return False

def take_photo():
    # Filename
    filename = datetime.now().strftime('%Y%m%d-%H%M%S.jpg') # Create filename by year, month, day, hour, minute and second

    try:
        greenOn()
        print("Start camera")
        camera = PiCamera()
        camera.resolution = (1024,768)
        # camera.resolution = (3280, 2464)
        # sleep(2)
        camera.capture(filename)
        print("Photo taken")
        greenOff()
    except:
        redOn()
        sleep(5)
        redOff()
        print("Camera mailfunction somehow")
    finally:
        camera.close()
        print("Camera close")

def upload():
    if is_connected() == True:
        blueOn()
        print("Start uploading image(s)")
        call("/home/pi/Dropbox-Uploader/dropbox_uploader.sh -s upload *.jpg /", shell=True)
        blueOff()
        print("Done uploading")

# Turn on LED
def ledOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    return True

def redOn():
    ledOn(redPin)

def greenOn():
    ledOn(greenPin)

def blueOn():
    ledOn(bluePin)

# Turn off LED
def ledOff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    return True

def redOff():
    ledOff(redPin)

def greenOff():
    ledOff(greenPin)

def blueOff():
    ledOff(bluePin)

try:
    while True: # loop foverver
        if(GPIO.input(18) == GPIO.LOW):
            take_photo()
            sleep(1)
        elif(GPIO.input(15) == GPIO.LOW):
            upload()
            sleep(1)
except KeyboardInterrupt:
    print("Interrupted")
