# Trash Classifier on RaspberryPI  
A component that can classify trash items into their category. Uses Python and runs on a raspberryPI system. 

# Hardware Component parts
## RaspberryPI:
The system was tested on RaspberryPI 3 model B.  
The operating system is RaspberryPI OS Debian. 11 Bullseye.   

## Camera:
The camera used is ArduCam OV5647 Mini Camera Module.  
It has a 5MP resolution.   
We take still pictures of 2592x1944 resolution  

## LCD screen:  
We used MHS3.5 LCD screen.   
To output to the screen, we needed the driver found here: https://github.com/goodtft/LCD-show
 
# Software Modules

## app.py
The main application entry points.  
Initializes the interface, the model, the camera, the hardware parts.  
Allows all classes to interact together.  

## camera.py
The camera has multiple functionalities including starting a preview, stopping the preview, taking a photo

## hardware.py 
This module is responsible for the 4 leds, blue for general , red for metal, yellow for paper, green for plastic

## interface.py

We used tkinter library to display the three different gui layouts, which are:

- The first layout: this layout will display bunch of text at the top, the camera frame, and the two buttons.
- The loading layout: this layout will display an animation which will present the loading. It keeps loading until 
  the model finishes its classification.
- The final layout: this layout will display the classfication result after the item has been classified by the model.
  It will display the name of the category and the percentage.

## model.py

### Model Training

The model is trained on several public datasets of trash from Kaggle including:
1. https://www.kaggle.com/datasets/naidusurajvardhan/recycling-waste
2. https://www.kaggle.com/datasets/sapal6/waste-classification-data-v2
3. https://www.kaggle.com/datasets/imrshu/solidwaste
4. https://www.kaggle.com/datasets/hseyinsaidkoca/recyclable-solid-waste-dataset-on-5-background-co


Our dataset consist of images in 6691 total divided into:
4685 for training 
959  for testing
1047 for validation

For the model we used `VVG19` as a backbone for our classification
The model can classify the images into one of 3 classes `plastic`, `paper`, and `metal`. 
Anything other than that with an accuracy less than **70%** is classified as general.

### Model class
`Model(file_path)` Constructor that takes the file path of the model and load it.

`load_model_(model_filepath)` takes the file path of the model and load it.

`predict_img_file(img_filepath, enable_saving = True, display_result = False)` takes the file path of the image, perform postprocessing, predict the class, and print the predictions.

`postprocess_preds_(preds, display_result=display_result)` print the list of predictions

`send_imgs_and_preds()` send the prediction results to the Raspberry Pi.

### Requirements of model class:
`TFLite` version 2.10.0 or above

`numpy` version 1.23.5 or above

`Pillow ` version 9.3.0 or above

`Python` version 3.9.2 or above



### Requirements:
- tkinter
- rpi.gpio
- picamera
- tflite
