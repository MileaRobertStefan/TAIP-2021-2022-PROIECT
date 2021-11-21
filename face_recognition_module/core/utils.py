import os

from mop.mop_decorators import event


@event
def save_image(image, filename):
    image.save(os.path.join('temp', filename))


@event
def delete_image(path):
    os.remove(path)
