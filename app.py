from interface import Interface
from camera import Camera
from model import Model
import time as t
class RaspberryPIManagement:
    def __init__(self):
        ## initialize objects
        self.camera = Camera(self)
        self.model = Model(self,model_filepath=r'./model/tf_lite_model.tflite')
        self.interface = Interface(self, self.exit_app,self.classify)
    ## define auxiliary functions
    def exit_app(self):
        quit()


        
    def receive_photo(self,img_path):
        self.interface.show_image(img_path)
        self.trigger_model(img_path)

    def make_stream(self):
        self.camera.stream()

    def classify(self):
        self.stop_stream()
        self.camera.take_photo()

    def stop_stream(self):
        self.camera.stop_stream()

    def trigger_model(self,img_path):
        self.model.predict_img_file(img_path)

    def receive_classification_data(self,dict):
        if dict['general']:
            self.leds.general_led()
        else:
            max_value = max(dict.values())  # maximum value
            max_key = [k for k, v in dict.items() if v == max_value][0]  # getting all keys containing the `maximum`
            if max_key == 'metal':
                self.leds.metaL_led()
            elif max_key == 'paper':
                self.leds.paper_led()
            else:
                self.leds.plastic_led()

        self.interface.display_classification_results(dict)



rpi_management = RaspberryPIManagement()
