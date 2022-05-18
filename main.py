import os

import cv2

from cascades.front_face import FrontFaceCascade
from cascades.profile_face import ProfileFaceCascade
from domain_objects.image import Image


def load_images_from_folder(folder: str) -> []:
    """Returns all images in a given folder"""
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            image = Image(image=img, name=filename)
            images.append(image)
    return images


def main():
    cascades = [FrontFaceCascade(), ProfileFaceCascade()]
    images = load_images_from_folder(folder='input')

    for img in images:
        for cascade in cascades:
            cascade.detect(img)
        cv2.imshow(img.name, img.image)
        cv2.waitKey()
        cv2.imwrite("output/" + img.name, img.image)


if __name__ == '__main__':
    main()
