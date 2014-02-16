class AbstractShredCreator(object):
    """
    This defines the interface.

    This takes an image and returns the shreds
    """

    def __init__(self):
        self.shreds = None

    def get_shreds(self, *args, **kwargs):
        """
        return shreds
        """
        return self.shreds

    def assemble(self, *args, **kwargs):
        pass