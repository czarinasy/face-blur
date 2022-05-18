import cv2


class FrontFaceCascade:
    def __init__(self):
        self.cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    def detect(self, img: []) -> None:
        """Detects front faces in an image"""
        grayscale_img = cv2.cvtColor(img.image, cv2.COLOR_BGR2GRAY)
        faces = self.cascade.detectMultiScale(image=grayscale_img, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces:
            # Get region of interest
            roi = img.image[y:y + h, x:x + w]
            blur = cv2.GaussianBlur(src=roi, ksize=(51, 51), sigmaX=0)
            # Insert ROI back into image
            img.blur_face(x, y, w, h, blur_region=blur)
