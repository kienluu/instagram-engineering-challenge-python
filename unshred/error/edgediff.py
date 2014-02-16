from itertools import izip, product, chain
from .base import AbstractPairErrorCalculator
from ..consts import WIDTH_KEY, HEIGHT_KEY


class EdgeDifferenceErrorCalculator(AbstractPairErrorCalculator):
    """
    Calculates the error along the vertical edges where two shreds join

    The error is calculated as the difference between the neighbouring pixels
    horizontally.
    """

    def get_error(self, left_shred, right_shred):
        left_edge = self.get_edge(right_shred.size[WIDTH_KEY] - 1, left_shred)
        right_edge = self.get_edge(0, right_shred)

        if isinstance(left_edge[0], tuple):
            return self.get_error_between_edges_of_tuples(left_edge, right_edge)

        return self.get_error_between_edges(left_edge, right_edge)


    @staticmethod
    def get_error_between_edges(left_edge, right_edge):
        error = 0
        for left_pixel, right_pixel in izip(left_edge, right_edge):
            error += abs(left_pixel - right_pixel)

        return error

    @staticmethod
    def get_error_between_edges_of_tuples(left_edge, right_edge):
        error = 0
        for left_pixel, right_pixel in izip(left_edge, right_edge):
            for l_dim, r_dim in izip(left_pixel, right_pixel):
                error += abs(l_dim - r_dim)

        return error

    @staticmethod
    def get_edge(x_const, shred):
        return [shred.getpixel((x_const,y))
                for y in xrange(shred.size[HEIGHT_KEY])]


class MatrixEdgeDifferenceErrorCalculator(AbstractPairErrorCalculator):
    """
    Calculates the error along the vertical edges where two shreds join

    The error is calculated as the difference between the neighbouring pixels
    horizontally.
    """

    # Create filter matrix and transpose for [x][y] access
    matrix = zip(*[
        [-1, 1],
        [-1, 1],
        [-1, 1],
    ])

    def __init__(self, matrix=None):
        if matrix:
            self.matrix = matrix

        self.matrix_width = len(self.matrix)
        self.matrix_height = len(self.matrix[0])

        self.matrix_radius = (self.matrix_height - 1 )/ 2
        self.d_y_map = range(-self.matrix_radius, self.matrix_radius + 1)

    def get_error(self, left_shred, right_shred):
        left_edge = self.get_edge(right_shred.size[WIDTH_KEY] - 1, left_shred)
        right_edge = self.get_edge(0, right_shred)

        if isinstance(left_edge[0], tuple):
            return self.get_error_between_edges_of_tuples(left_edge, right_edge)

        return self.get_error_between_edges(left_edge, right_edge)

    def get_error_between_edges(self, left_edge, right_edge):
        height = len(left_edge)
        error = 0

        for y_offset in xrange(self.matrix_radius, height - self.matrix_radius):
            error += self.get_error_at_y(
                y_offset, left_edge, right_edge)

        return error

    def get_error_between_edges_of_tuples(
            self, source_left_edge, source_right_edge):
        num_dim = len(source_left_edge[0])
        error = 0

        for index in xrange(num_dim):
            left_edge = [pixel[index] for pixel in source_left_edge]
            right_edge = [pixel[index] for pixel in source_right_edge]
            error += self.get_error_between_edges(left_edge, right_edge)

        return error

    def get_error_at_y(self, target_y_offset, left_edge, right_edge):
        data = (left_edge, right_edge)
        value = 0

        # TODO: Find out of product is lazy
        for m_x, m_y in product(
                xrange(self.matrix_width), xrange(self.matrix_height)):
            coefficient = self.matrix[m_x][m_y]
            y_offset = target_y_offset + self.d_y_map[m_y]
            value += data[m_x][y_offset] * coefficient

        return abs(value)

    @staticmethod
    def get_edge(x_const, shred):
        return [shred.getpixel((x_const,y))
                for y in xrange(shred.size[HEIGHT_KEY])]
