from PIL import Image
from unshred.error.base import AbstractPairErrorCalculator
from unshred.error.edgediff import EdgeDifferenceErrorCalculator
from unshred.shredmaker.fixedwidth import FixedWidthVerticalShredMaker
from unshred.unshredder.spanton import SpantonUnshredder


class InvalidErrorClassException(Exception):
    pass


def create_simple_unshredder(
        image_path, shred_width,
        error_calculator_class=EdgeDifferenceErrorCalculator,
        error_calculator_args=()):
    """
    Returns a unshredder with these behaviors:
    unshredder: SpantonUnshredder
    error_calculator: EdgeDifferenceErrorCalculator
        or any AbstractPairErrorCalculator instance
    shred_maker: FixedWidthVerticalShredMaker
    """
    if not issubclass(error_calculator_class, AbstractPairErrorCalculator):
        raise InvalidErrorClassException

    image = Image.open(image_path)
    shred_maker = FixedWidthVerticalShredMaker()
    error_calculator = error_calculator_class(*error_calculator_args)
    unshredder = SpantonUnshredder(
        image, error_calculator, shred_maker, shred_width)
    return unshredder