import logging
import sys
from unshred.error.edgediff import NormalisedMatrixEdgeDifferenceErrorCalculator
from unshred.factory.simple import create_simple_unshredder

ch = logging.StreamHandler(stream=sys.stdout)
logger = logging.getLogger('unshredder')
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)


def main():
    matrix = zip(*[
        [-1, 1],
        [-1, 1],
        [-1, 1],
        [-1, 1],
        [-1, 1],
    ])

    unshredder = create_simple_unshredder(
        'assets/shredded_images/TokyoPanoramaShredded.png', 32,
        error_calculator_class=NormalisedMatrixEdgeDifferenceErrorCalculator,
        error_calculator_args=(matrix,))
    answer = unshredder.solve()
    answer.save('output/matrix_answer.png')

if __name__ == "__main__":
    main()