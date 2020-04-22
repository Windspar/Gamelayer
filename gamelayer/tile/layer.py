from itertools import zip_longest

class TileLayer:
    layers = ["ground", "object"]

    def __init__(self, *args):
        zip_data = zip_longest(TileLayer.layers, args, fillvalue=None)
        self.layer = dict([(key, image) for key, image in zip_data])
        self.image = None

    def blend(self):
        key = TileLayer.layers[0]
        if self.layer[key]:
            self.image = self.layer[key].copy()
        else:
            self.image = None
            return

        for key in TileLayer.layers[1:]:
            image = self.layer[key]
            if image:
                self.image.blit(image, (0, 0))

    def draw(self, surface, position):
        if self.image is None:
            self.blend()

        if self.image:
            position = tuple(map(int, position))
            surface.blit(self.image, position)

    def __setitem__(self, key, value):
        self.layer[key] = value
