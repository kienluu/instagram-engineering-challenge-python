import unittest
from ..edgediff import EdgeDifferenceErrorCalculator


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

        self.assertEqual(
            EdgeDifferenceErrorCalculator.get_error_between_edges(
                left_edge, right_edge), 4)

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
                left_edge, right_edge), 6)