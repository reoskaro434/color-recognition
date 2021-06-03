from tensorflow.python.keras.preprocessing import image
from image_recognizer.image_recognizer_interface import ImageRecognizerInterface
import numpy as np
import tensorflow as tf


class ImageRecognizer(ImageRecognizerInterface):

    def __init__(self):
        self._model = tf.keras.models.load_model("color_recognizer.model")

    def _get_color_name(self, color_vector) -> str:

        is_one = False
        argument = -1
        for idx, val in enumerate(color_vector[0]):
            if val == 1:
                if not is_one:
                    is_one = True
                    argument = idx
                else:
                    argument = -1
                    break

        color_descriptor = {
            0: "black",
            1: "blue",
            2: "brown",
            3: "green",
            4: "orange",
            5: "red",
            6: "violet",
            7: "white",
            8: "yellow"
        }

        return color_descriptor.get(argument, "color not recognized")

    def recognize_image(self, image_path) -> str:
        current_image = tf.keras.preprocessing.image.load_img(
            image_path,
            target_size=(200, 200)
        )

        # prepare image for recognition
        image_array = image.img_to_array(current_image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = np.vstack([image_array])

        color_vector = self._model.predict(image_array)
        return self._get_color_name(color_vector)
