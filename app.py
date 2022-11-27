from interface import Interface
from camera import Camera
from model import Model
class RaspberryPIManagement:
    def __init__(self):
        ## initialize objects
        self.camera = Camera(self)
        self.model = Model(self)
        self.interface = Interface(self, self.exit_app,self.classify,"Trash Classifier")
        self.interface.show()

    ## define auxiliary functions
    def exit_app(self):
        quit()

    def classify(self):
        self.camera.take_photo()
    def receive_photo(self,img_path):
        self.interface.show_image(img_path)

rpi_management = RaspberryPIManagement()

    