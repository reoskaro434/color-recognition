from abc import ABC, abstractmethod


class ImageRecognizerInterface(ABC):

    @abstractmethod
    def recognize_image(self, image_path):
        pass
