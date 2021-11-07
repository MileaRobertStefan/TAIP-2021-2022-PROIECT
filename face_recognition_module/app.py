import json
import os
import random
import face_recognition
from flask import Flask, request

from services.face_detection_service import FaceDetectionService
from services.face_recognition_service import FaceRecognitionService

app = Flask(__name__)


def get_random_filename():
    return str(random.randint(0, 10000000))


@app.route("/detection", methods=['POST'])
def detection():
    image = request.files['photo']
    if '.' in image.filename:
        filename = get_random_filename() + '.' + image.filename.rsplit('.', 1)[1].lower()
        image.save(os.path.join('temp', filename))

        image = face_recognition.load_image_file("./temp/" + filename)

        result = FaceDetectionService.get_faces(image)

        os.remove("./temp/"+filename)
        return json.dumps(result.__dict__, default=lambda k: k.__dict__)
    return "400"


@app.route("/recognition", methods=['POST'])
def recognition():
    image = request.files['photo']
    identity = request.files['identity']
    if '.' in image.filename and '.' in identity.filename:
        image_filename = get_random_filename() + '.' + image.filename.rsplit('.', 1)[1].lower()
        identity_filename = get_random_filename() + '.' + identity.filename.rsplit('.', 1)[1].lower()
        image.save(os.path.join('temp', image_filename))
        identity.save(os.path.join("temp", identity_filename))

        image = face_recognition.load_image_file("./temp/" + image_filename)
        identity = face_recognition.load_image_file("./temp/" + identity_filename)

        result = FaceRecognitionService.get_faces(identity_image=identity, image=image)

        os.remove("./temp/"+image_filename)
        os.remove("./temp/"+identity_filename)
        return json.dumps(result.__dict__, default=lambda k: k.__dict__)
    return "400"


if __name__ == '__main__':
    app.run()
