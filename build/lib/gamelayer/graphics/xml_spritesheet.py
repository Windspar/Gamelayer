import xml.etree.ElementTree as ET
from pygame import Rect
from pygame.image import load as image_load
from pygame.transform import scale as image_scale

DEFAULT_ATTRIBUTES = ["x", "y", "width", "height"]
DEFAULT_KEY = "name"

class XmlSpriteSheet:
    def __init__(self, filename, alpha, xmlfile, scale_by=1, attributes=DEFAULT_ATTRIBUTES, key=DEFAULT_KEY):
        self.attributes = attributes
        self.scale_by = scale_by
        self.key = key
        self.read_xml(xmlfile)
        self.load(filename, alpha)

    def load(self, filename, alpha):
        self.sprite_sheet = image_load(filename)
        if alpha:
            self.sprite_sheet = self.sprite_sheet.convert_alpha()
        else:
            self.sprite_sheet = self.sprite_sheet.convert()

        if self.scale_by != 1:
            size = self.sprite_sheet.get_size()
            size = int(size[0] // self.scale_by), int(size[1] // self.scale_by)
            self.sprite_sheet = image_scale(self.sprite_sheet, size)

    def read_xml(self, xmlfile):
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        self.xml_tree = {}

        for child in root:
            rect = Rect([int(child.get(attrib)) // self.scale_by for attrib in self.attributes])
            self.xml_tree[child.get(self.key)[:-4]] = rect

    def __getitem__(self, key):
        if key in self.xml_tree.keys():
            return self.sprite_sheet.subsurface(self.xml_tree[key])
