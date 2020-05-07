from pygame import Vector2

class AnchorPosition:
    def __init__(self, sprite, position, anchor):
        self.sprite = sprite
        self.anchor = anchor
        self.position = position

    def apply(self):
        self.sprite.rect = self.sprite.image.get_rect(**{self.anchor: self.position})
        self.sprite._center = Vector2(self.sprite.rect.center)

    def apply_anchor(self, anchor):
        setattr(self.sprite.rect, anchor, self.position)

    def set_position(self, position, anchor):
        if anchor:
            self.anchor = anchor

        self.position = position
        setattr(self.sprite.rect, self.anchor, self.position)
