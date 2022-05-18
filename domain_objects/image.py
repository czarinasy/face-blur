class Image:
    """Saves an image coordinate with its filename"""
    def __init__(self, image: [], name: str):
        self.image = image
        self.name = name

    def blur_face(self, x: int, y: int, w: int, h: int, blur_region: []) -> None:
        """Blurs a region of interest"""
        self.image[y:y + h, x:x + w] = blur_region
