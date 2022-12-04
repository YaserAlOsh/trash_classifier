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


## interface.py

## model.py



### Requirements:
- guizero
- rpi.gpio
- picamera
- tflite
