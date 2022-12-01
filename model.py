import numpy as np
import tensorflow as tf
from tensorflow import keras


class Model():

    def __init__(self, model_filepath):  # load the model from disk, must be a path to model dir

        self.model_filepath = model_filepath
        self._load_model_(self.model_filepath)
        self.predictions = None
        self.train_ds = None
        self.test_ds = None

    def __str__(self):
        self.model_checkpoint.summary()
        return ""

    def _load_model_(self, model_filepath):
        print("Loading model ...")
        self.model_checkpoint = keras.models.load_model(filepath=model_filepath)
        print("Model loaded.")

    def update_model(self, batch_size=16, epochs=10):  # to re-train the model, data must be loaded first
        if self.train_ds is None:
            print("No data has been loaded for training, consider using .load_data()")

        else:
            print("The model is updating")
            self.model_checkpoint.fit(self.train_ds, batch_size=batch_size, epochs=epochs)
            self.model_checkpoint.save(self.model_filepath)
            print(f"The model has finished updating, model saved to {self.model_filepath}")

    def test_model(self):  # to test the model, data must be loaded first
        if self.test_ds is None:
            print("No data has been loaded for testing, consider using .load_data()")
        else:
            self.model_checkpoint.evaluate(x_test, y_test)

    def predict_img_arr(self, img_arr, enable_saving=False):  # presumes that the input array is (256, 256, 3)
        if len(img_arr.shape) == 3:
            img_arr = np.expand_dims(img_arr, axis=0)
            preds = self.model_checkpoint.predict(img_arr)
            return preds

            if enable_saving:
                self._postprocess_preds_(preds)
        else:
            print("Image array not in right format. Must be array with the following dimensions: (256, 256, 3)")

    def predict_img_file(self, img_filepath, enable_saving=True, display_result=False):  # predict from an image file
        img_name = img_filepath.split('\\')[-1]
        print(f"Predicting the class of image: {img_name}..")

        img = keras.utils.load_img(path=img_filepath)
        img = img.resize(size=(256, 256))
        img_arr = keras.utils.img_to_array(img)
        preds = self.predict_img_arr(img_arr)

        if enable_saving:
            self._postprocess_preds_(preds, display_result=display_result)

    def load_data(self, train_dir=None,
                  test_dir=None):  # loads from directories divided into more directories per class containing the images
        if train_dir is not None:
            self.train_ds = keras.utils.image_dataset_from_directory(directory=train_dir,
                                                                     label_mode='categorical')
        if test_dir is not None:
            self.test_ds = keras.utils.image_dataset_from_directory(directory=test_dir,
                                                                    label_mode='categorical')
        print("loaded specified data successfully")

    def _postprocess_preds_(self, preds_arr, display_result=False):
        preds_arr = preds_arr[0]
        label_map = {'Metal': preds_arr[0], 'Paper': preds_arr[1], 'Plastic': preds_arr[2]}
        self.predictions = label_map
        if display_result:
            print(
                f"Metal: {self.predictions['Metal'] * 100}% \nPaper: {self.predictions['Paper'] * 100}% \nPlastic: {self.predictions['Plastic'] * 100}%\n")



