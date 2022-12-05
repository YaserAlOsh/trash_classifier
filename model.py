#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from PIL import Image

# import tensorflow as tf
import tflite_runtime.interpreter as tflite  # needs testing


# In[2]:


class Model():

    def __init__(self, rpi, model_filepath):
        self.model_filepath = model_filepath
        self.predictions = None
        self.rpi = rpi  # needs testing
        self._load_model_(self.model_filepath)

    def _load_model_(self, model_filepath):
        print("Loading model ...")
        self.interpreter = tflite.Interpreter(model_path=model_filepath)  # needs testing
        self.interpreter.allocate_tensors()
        self.intrp_input_details = self.interpreter.get_input_details()
        self.intrp_output_details = self.interpreter.get_output_details()
        print("Model loaded.")

    def predict_img_file(self, img_filepath, enable_saving=True, display_result=False):
        img = Image.open(img_filepath)
        img.load()
        img = img.resize(size=(256, 256))
        img_arr = np.array(img, dtype=np.float32)
        img_arr = np.expand_dims(img_arr, axis=0)
        print(img_arr.shape)
        assert img_arr.shape == (1, 256, 256, 3)

        self.interpreter.set_tensor(self.intrp_input_details[0]['index'], img_arr)
        self.interpreter.invoke()
        preds = self.interpreter.get_tensor(self.intrp_output_details[0]['index'])

        if enable_saving:
            self._postprocess_preds_(preds, display_result=display_result)
        self.send_imgs_and_preds()
    def _postprocess_preds_(self, preds_arr, display_result=False):
        preds_arr = preds_arr[0]
        label_map = {'Metal': preds_arr[0], 'Paper': preds_arr[1], 'Plastic': preds_arr[2], 'General': False}

        if label_map['Metal'] <= 0.7 and label_map['Paper'] <= 0.7 and label_map['Plastic'] <= 0.7:
            label_map['General'] = True

        self.predictions = label_map
        if display_result:
            print(
                f"Metal: {self.predictions['Metal'] * 100}% \nPaper: {self.predictions['Paper'] * 100}% \nPlastic: {self.predictions['Plastic'] * 100}%\nGeneral: {self.predictions['General']}\n")

    # needs testing
    def send_imgs_and_preds(self):
        self.rpi.receive_classification_data(self.predictions)

