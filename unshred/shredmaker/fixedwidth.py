from unshred.shredmaker.base import AbstractShredMaker


class FixedWidthVerticalShredMaker(AbstractShredMaker):

    def get_shreds(self, image, shred_width):
        return []