from picamera import PiCamera
from time import sleep

class Camera:
    temp_photo_path = 'temp.png'
    camera = None
    def __init__(self,rpi):
        self.camera = PiCamera()
        self.camera.rotation=180
        self.temp_photo_path = 'temp.png'
        self.rpi = rpi
    def take_photo(self):
        sleep(2)
        self.camera.capture(self.temp_photo_path)
        self.rpi.receive_photo(self.temp_photo_path)
        print("Done.")
