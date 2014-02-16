from PIL import Image
from ..shred.base import WIDTH_KEY, HEIGHT_KEY
from .base import AbstractShredMaker


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
        if not isinstance(shreds, list):
            shreds = list(shreds)

        first_shred = shreds[0]
        height = first_shred.size[HEIGHT_KEY]
        width = sum((shred.size[WIDTH_KEY]for shred in shreds), 0)
        image = Image.new(first_shred.mode, (width, height))

        x_offset = 0

        for shred in shreds:
            image.paste(shred, (x_offset, 0))
            x_offset += shred.size[WIDTH_KEY]

        return image