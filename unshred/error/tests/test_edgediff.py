import unittest
from ..edgediff import EdgeDifferenceErrorCalculator, MatrixEdgeDifferenceErrorCalculator


class TestEdgeDiff(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_error_between_edges(self):
        left_edge = [10, 10, 5, 5]
        right_edge = [10, 10, 5, 5]

        self.assertEqual(
            EdgeDifferenceErrorCalculator.get_error_between_edges(
                left_edge, right_edge), 0)

        left_edge = [8, 12, 5, 5]
        right_edge = [10, 10, 5, 5]

        self.assertAlmostEqual(
            EdgeDifferenceErrorCalculator.get_error_between_edges(
                left_edge, right_edge), 2 / 30.0, places=15)

    def test_get_error_between_edges_of_tuples(self):
        left_edge = [(10, 10, 10), (5, 5, 5)]
        right_edge = [(10, 10, 10), (5, 5, 5)]

        self.assertEqual(
            EdgeDifferenceErrorCalculator.get_error_between_edges_of_tuples(
                left_edge, right_edge), 0)

        left_edge = [(9, 9, 9), (4, 4, 4)]
        right_edge = [(10, 10, 10), (5, 5, 5)]

        self.assertEqual(
            EdgeDifferenceErrorCalculator.get_error_between_edges_of_tuples(
                left_edge, right_edge), 0.07142857142857142)

class TestMatrixEdgeDifferenceErrorCalculator(unittest.TestCase):

    def test_get_error_at_y(self):
        error_calc = MatrixEdgeDifferenceErrorCalculator()

        left_edge = [1, 2, 2, 2]
        right_edge = [1, 2, 2, 2]
        self.assertEqual(error_calc.get_error_at_y(1, left_edge, right_edge), 0)

        left_edge = [10, 10, 10]
        right_edge = [1, 1, 1]
        self.assertEqual(error_calc.get_error_at_y(
            1, left_edge, right_edge), 30 - 3)

        left_edge = [10, 1, 10]
        right_edge = [1, 10, 1]
        self.assertEqual(error_calc.get_error_at_y(
            1, left_edge, right_edge), 21 - 12)

        left_edge = [10, 1, 10, 1]
        right_edge = [1, 10, 1, 10]
        self.assertEqual(error_calc.get_error_at_y(
            2, left_edge, right_edge), 21 - 12)

    def test_get_error_between_edges(self):
        error_calc = MatrixEdgeDifferenceErrorCalculator()

        left_edge = [1, 2, 2, 2]
        right_edge = [1, 2, 2, 2]
        self.assertEqual(error_calc.get_error_between_edges(
            left_edge, right_edge), 0)

        left_edge = [10, 10, 10, 10]
        right_edge = [1, 1, 1, 1]
        self.assertEqual(error_calc.get_error_between_edges(
            left_edge, right_edge), 54)


        left_edge = [10, 1, 10, 1]
        right_edge = [1, 10, 1, 10]
        self.assertEqual(error_calc.get_error_between_edges(
            left_edge, right_edge), 18)