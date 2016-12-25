from time import sleep
from datetime import datetime
from picamera import PiCamera
from subprocess import call
import socket

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
    filename = datetime.now().strftime('%Y%m%d-%H%M%S.jpg')

    try:
        print("Start camera")
        camera = PiCamera()
        # camera.resolution = (1024,768)
        camera.resolution = (3280, 2464)
        # sleep(2)
        camera.capture(filename)
        print("Photo taken")
    except:
        print("Camera mailfunction somehow")
    finally:
        camera.close()
        print("Camera close")

def upload():
    if is_connected() == True:
        print("Start uploading image")
        call("/home/pi/Dropbox-Uploader/dropbox_uploader.sh -s upload *.jpg /", shell=True)
        print("Done uploading")


take_photo()
upload()
