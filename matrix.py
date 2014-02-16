from unshred.error.edgediff import MatrixEdgeDifferenceErrorCalculator
from unshred.factory.simple import create_simple_unshredder


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
        error_calculator_class=MatrixEdgeDifferenceErrorCalculator,
        error_calculator_args=(matrix,))
    answer = unshredder.solve()
    answer.save('output/matrix_answer.png')

if __name__ == "__main__":
    main()