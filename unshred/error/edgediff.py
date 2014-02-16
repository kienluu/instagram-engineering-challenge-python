from itertools import izip
import math
from unshred.error.base import AbstractErrorCalculator
from unshred.shred.base import WIDTH_KEY, HEIGHT_KEY


class EdgeDifferenceErrorCalculator(AbstractErrorCalculator):
    """
    Calculates the error along the vertical edges where two shreds join

    The error is calculated as the difference between the neighbouring pixels
    horizontally.
    """

    def get_error(self, left_shred, right_shred):
        left_edge = self.get_edge(0, left_shred)
        right_edge = self.get_edge(
            right_shred.image.size[WIDTH_KEY], right_shred)

        if isinstance(left_edge[0], tuple):
            return self.get_error_between_edges_of_tuples(left_edge, right_edge)

        return self.get_error_between_edges(left_edge, right_edge)


    @staticmethod
    def get_error_between_edges(left_edge, right_edge):
        error = 0
        for left_pixel, right_pixel in izip(left_edge, right_edge):
            if isinstance(left_pixel, tuple):
                for l_dim, r_dim in izip(left_pixel, right_pixel):
                    error += math.fabs(l_dim - r_dim)
            else:
                error += math.fabs(left_pixel - right_pixel)

        return error

    @staticmethod
    def get_error_between_edges_of_tuples(left_edge, right_edge):
        error = 0
        for left_pixel, right_pixel in izip(left_edge, right_edge):
            for l_dim, r_dim in izip(left_pixel, right_pixel):
                error += math.fabs(l_dim - r_dim)

        return error

    @staticmethod
    def get_edge(x_const, shred):
        return [shred.getpixel((x_const,y))
                for y in xrange(shred.size[HEIGHT_KEY])]