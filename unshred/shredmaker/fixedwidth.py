from unshred.shredmaker.base import AbstractShredMaker


class SmallerWidthException(Exception):
    pass


class FixedWidthVerticalShredMaker(AbstractShredMaker):

    def __init__(self, force_perfect_fit=True):
        self.force_perfect_fit = force_perfect_fit

    def get_shreds(self, image, shred_width):
        return []