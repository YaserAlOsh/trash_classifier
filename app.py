from interface import Interface
from camera import Camera
from model import Model
class RaspberryPIManagement:
    def __init__(self):
        ## initialize objects
        self.camera = Camera(self)
        self.model = Model(self)
        self.interface = Interface(self, self.exit_app,self.trigger_camera,"Trash Classifier")
        self.interface.show()

    ## define auxiliary functions
    def exit_app(self):
        quit()

    def trigger_camera(self):
        self.camera.stop_preview()
        self.camera.myfile.close()
        self.camera.take_photo()
        
    def receive_photo(self,img_path):
        self.interface.show_image(img_path)
    
    def trigger_model(self,img_path):
        self.model.predict_img_file(img_path)
    def receive_classification_data(self,dict):
        self.interface.display_classification_results(dict)
        


rpi_management = RaspberryPIManagement()

    
