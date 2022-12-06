from interface import Interface
from app import RaspberryPIManagement
from camera import Camera
from model import Model
import time


### Run Unit Test cases sequentially
## This creates the interface and shows it on screen.
interface = Interface(None)
## This starts the loading panel.
interface.display_loading_layout()

time.sleep(3)
## This shows a dummy classification result
interface.display_classification_results({'General':False,'Metal':0.98,'Plastic':0.05,'Paper':0.01})

## This creates a camera object
camera = Camera(None)
## This starts the live-stream preview
camera.stream()

time.sleep(3)
## This stops teh live-stream preview
camera.stop_stream()

## This creates a model object, and gives it the path to the store tflite model:
model = Model(model_filepath=r'./model/tf_lite_model.tflite')

## images to test for:
images = [('paper_image.jpg',['Paper']),('metal_plastic.jpg',['Metal','Plastic'])]

def getMaxCategory(dict):
    if dict['General']==True:
            return 'General'
    else:
        max_value = max(dict.values())  # maximum value
        if dict['Metal'] == max_value:
            return 'Metal'
        elif dict['Paper'] == max_value:
            return 'Paper'
        else:
            return 'Plastic'

## For each test image:
for img_path,cat in images:
    ## This asks the model to predict the category of the image
    model.predict_img_file(img_path,enable_saving=True)
    ## Assert that the category with the maximum predicted category is in the test case allowed categories:
    assert getMaxCategory(model.predictions) in cat


### Integrated Testing: (Only run this on the RaspberryPI system)
rpi = RaspberryPIManagement()
### Start the classification process
rpi.interface.call_classify_and_loading()



