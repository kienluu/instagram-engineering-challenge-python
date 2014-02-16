class AbstractErrorCalculator(object):
    """
    Interface for ErrorCalculator
    """
    def get_error(self, *args, **kwargs):
        pass


class AbstractPairErrorCalculator(object):

    def get_error(self, left, right):
        pass