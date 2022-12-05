from picamera import PiCamera
from time import sleep

class Camera:
    temp_photo_path = 'temp.jpg'
    camera = None
    def __init__(self,rpi):
        self.camera = PiCamera()
        self.camera.rotation=180
        self.temp_photo_path = 'temp.jpg'
        self.rpi = rpi
        self.my_file = ""
        
    def take_photo(self):
        self.camera.capture(self.temp_photo_path)
        self.rpi.receive_photo(self.temp_photo_path)
        print("Done.")

    def stream(self):
        self.my_file = open("my_file.jpg","wb")
        self.camera.start_preview(fullscreen=False,window=(0,0,300,400))

    def stop_stream(self):
        self.camera.stop_preview()
        self.my_file.close()
