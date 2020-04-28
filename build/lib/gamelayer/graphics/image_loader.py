from pathlib import Path
from os import listdir, path
from pygame.image import load as image_load
from pygame.transform import scale as image_scale


DEFAULT_IMAGE_TYPES = "bmp", "png", "jpg", "gif"

class ImageLoader:
    def __init__(self, location, alpha=False, image_types=DEFAULT_IMAGE_TYPES, scale=None):
        self.images = {}
        self.load(location, alpha, image_types, scale)

    def __getitem__(self, key):
        return self.images[key]

    def clear(self):
        self.images = {}

    def load(self, location, alpha=False, image_types=DEFAULT_IMAGE_TYPES, scale=None):
        location = Path(location)
        if location.exists():
            files = listdir(location)
            for file in files:
                file = Path(file)
                if file.suffix[1:] in image_types:
                    filename = path.join(location, file)
                    image = image_load(filename)

                    if scale:
                        image = image_scale(image, scale)

                    if alpha:
                        image = image.convert_alpha()
                    else:
                        image = image.convert()

                    self.images[file.stem] = image
