from collections import namedtuple
from .base import Unshredder

ShredPair = namedtuple('ShredPair', 'left_shred right_shred error')
ShredPath = namedtuple('ShredPath', 'shred_order error')


class SpantonUnshredder(Unshredder):
    """
    INTRO:

    Named after Dave Spanton because he was the first to give me the idea.
    Its probably similar to his github solution for the Instagram challenge
    that he has done in factor:

    https://github.com/davespanton/factor-instagram-the-unshred

    DESCRIPTION:

    This is a unshredding algorithm for images that have been sliced
    vertically/horizontally only.

    It will build a 2d table of errors for each left shred and right shred pair.
    The algorithm will pick a shred then pick its pair that has
    the lowest error, and with that right shred, find its right neighbour with
    the lowest error until all shred are used.  The sum of these error is the
    paths error.  The algorithm will find the path error for each starting
    thread.  The path with the lowest path error is assumed to be the solution
    """

    def __init__(self, image, error_calculator, shred_maker, shred_width):
        self.image = image
        self.error_calculator = error_calculator
        self.shred_maker = shred_maker
        self.shred_width = shred_width
        self.shreds = None
        self.pair_table = None

    def solve(self):
        self.shreds = self.shred_maker.get_shreds(self.image, self.shred_width)

        self.create_pair_table()

        return self.shred_maker.assemble(
            self.find_lowest_error_path().shred_order)

    def create_pair_table(self):
        pair_table = {}
        for left_shred in self.shreds:
            left_shred_table = pair_table[left_shred] = {}
            for right_shred in self.shreds:
                if left_shred is right_shred:
                    continue

                left_shred_table[right_shred] = \
                    ShredPair(
                        left_shred, right_shred,
                        self.error_calculator.get_error(
                            left_shred, right_shred))

        self.pair_table = pair_table

    def get_lowest_error_pair(self, left_shred, available_shreds):
        left_shred_pair_table = self.pair_table[left_shred]
        lowest_error_pair = left_shred_pair_table[available_shreds[0]]

        for right_shred in available_shreds:
            if left_shred_pair_table[right_shred].error < lowest_error_pair.error:
                lowest_error_pair = left_shred_pair_table[right_shred]

        return lowest_error_pair

    def get_path_error(self, start_shred):
        available_shreds = list(self.shreds)
        available_shreds.remove(start_shred)
        shred_order = [start_shred]

        left_shred = start_shred
        total_error = 0

        while available_shreds:
            lowest_error_pair = self.get_lowest_error_pair(
                left_shred, available_shreds)

            print len(available_shreds)

            available_shreds.remove(lowest_error_pair.right_shred)
            shred_order.append(lowest_error_pair.right_shred)

            left_shred = lowest_error_pair.right_shred
            total_error += lowest_error_pair.error

        return ShredPath(shred_order, total_error)

    def find_lowest_error_path(self):
        best_path = None

        for start_shred in self.shreds:
            path = self.get_path_error(start_shred)
            if not best_path:
                best_path = path
            else:
                if path.error < best_path.error:
                    best_path = path

        return best_path
