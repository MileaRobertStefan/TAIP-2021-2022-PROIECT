import json
import os
import random
from flask import Flask, request
from flask_cors import CORS

from core.utils import save_image, delete_image
from services.face_detection_service import FaceDetectionService
from services.face_recognition_service import FaceRecognitionService

app = Flask(__name__)
CORS(app)


def get_random_filename():
    return str(random.randint(0, 10000000))


@app.route("/detection", methods=['POST'])
def detection():
    image = request.files['photo']
    if '.' in image.filename:
        filename = get_random_filename() + '.' + image.filename.rsplit('.', 1)[1].lower()
        save_image(image, filename)

        result = FaceDetectionService.get_faces("./temp/" + filename)

        delete_image("./temp/" + filename)

        return json.dumps(result.__dict__, default=lambda k: k.__dict__)
    return "400"


@app.route("/recognition", methods=['POST'])
def recognition():
    image = request.files['photo']
    identity = request.files['identity']
    if '.' in image.filename and '.' in identity.filename:
        image_filename = get_random_filename() + '.' + image.filename.rsplit('.', 1)[1].lower()
        identity_filename = get_random_filename() + '.' + identity.filename.rsplit('.', 1)[1].lower()

        save_image(image, image_filename)
        save_image(identity, identity_filename)

        result = FaceRecognitionService.get_recognized_faces("./temp/" + image_filename, "./temp/" + identity_filename)

        delete_image("./temp/" + image_filename)
        delete_image("./temp/" + identity_filename)

        return json.dumps(result.__dict__, default=lambda k: k.__dict__)
    return "400"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
