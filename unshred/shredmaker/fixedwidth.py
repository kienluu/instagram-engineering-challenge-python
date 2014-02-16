from PIL.Image import Image
from unshred.shred.base import WIDTH_KEY, HEIGHT_KEY
from unshred.shredmaker.base import AbstractShredMaker


class SmallerWidthException(Exception):
    pass


class FixedWidthVerticalShredMaker(AbstractShredMaker):

    def __init__(self, force_perfect_fit=True):
        self.force_perfect_fit = force_perfect_fit

    def get_shreds(self, image, shred_width):
        if self.force_perfect_fit and image.size[WIDTH_KEY] % shred_width != 0:
            raise SmallerWidthException

        # img.crop(0,0,1,1) returns a 1 pixel image of the first pixel at 0,0
        return [image.crop(
                (x, 0, x + shred_width, image.size[HEIGHT_KEY]))
                for x in xrange(0, image.size[WIDTH_KEY], shred_width)]

    def assemble(self, shreds):
        return Image()