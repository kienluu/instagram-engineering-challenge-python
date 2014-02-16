from itertools import imap, izip
import unittest
import os
from PIL import Image
from unshred.shredmaker.fixedwidth import FixedWidthVerticalShredMaker, SmallerWidthException

MODULE_DIR = os.path.dirname(__file__)


class TestFixedWidthVerticalShredMaker(unittest.TestCase):

    def setUp(self):
        source_path = os.path.join(
            MODULE_DIR, 'assets', 'source', 'TokyoPanoramaShredded.png')
        self.source_image = Image.open(source_path)


    def test_raise_smaller_width_exception(self):
        shred_width = 33

        shred_maker = FixedWidthVerticalShredMaker()

        with self.assertRaises(SmallerWidthException):
            shreds = shred_maker.get_shreds(self.source_image, shred_width)

    def test_shredding(self):
        shred_width = 32

        expected_shred_paths = \
            imap(lambda x: '%s/assets/shreds/%s.png' % (MODULE_DIR, x),
                 range(0, 640, shred_width))

        expected_shreds = imap(
            lambda path: Image.open(path), expected_shred_paths)

        shred_maker = FixedWidthVerticalShredMaker()
        shreds = shred_maker.get_shreds(self.source_image, shred_width)

        self.assertEqual(len(shreds), 20, '20 shreds was expected')

        error_msg = 'shred did not match expected shred file %s'
        for shred, expected_shred in izip(shreds, expected_shreds):
            self.assertEqual(shred.tobytes(), expected_shred.tobytes(),
                             error_msg % expected_shred.filename)
