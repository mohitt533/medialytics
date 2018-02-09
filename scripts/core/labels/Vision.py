from google.cloud import vision
from google.cloud.vision import types
import io
import json
from .Helpers import Helper


class Vision(object):
    google_vision_client = vision.ImageAnnotatorClient()
    image_path = ''
    result = {}

    @staticmethod
    def get_data(path):
        with io.open(path, 'rb') as image_file:
            data = image_file.read()
        return data

    @classmethod
    def detect_labels(cls, img):
        cls.image_path = '{}'.format(img)
        data = cls.get_data(cls.image_path)
        vision_image = types.Image(content=data)
        label_detection = cls.google_vision_client.label_detection(image=vision_image)
        labels = label_detection.label_annotations
        safe_search = cls.google_vision_client.safe_search_detection(image=vision_image)
        safe_annotations = safe_search.safe_search_annotation
        likelihood = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')

        #label notations
        cls.result = Helper.get_desc(labels)

        # safe notations
        cls.result['adult'] = likelihood[safe_annotations.adult]
        cls.result['violence'] = likelihood[safe_annotations.violence]
        print(json.dumps(cls.result))
        return json.dumps(cls.result)
