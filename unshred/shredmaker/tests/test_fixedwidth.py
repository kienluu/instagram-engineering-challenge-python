from itertools import imap, izip
import unittest
import os
from PIL import Image
from unshred.shredmaker.fixedwidth import FixedWidthVerticalShredMaker, \
    SmallerWidthException

MODULE_DIR = os.path.dirname(__file__)


class TestFixedWidthVerticalShredMaker(unittest.TestCase):

    def setUp(self):
        source_path = os.path.join(
            MODULE_DIR, 'assets', 'source', 'TokyoPanoramaShredded.png')
        self.source_image = Image.open(source_path)
        self.shred_width = 32

        expected_shred_paths = \
            imap(lambda x: '%s/assets/shreds/%s.png' % (MODULE_DIR, x),
                 range(0, 640, self.shred_width))

        self.expected_shreds = imap(
            lambda path: Image.open(path), expected_shred_paths)

        self.shred_maker = FixedWidthVerticalShredMaker()


    def test_raise_smaller_width_exception(self):
        shred_width = 33

        with self.assertRaises(SmallerWidthException):
            shreds = self.shred_maker.get_shreds(self.source_image, shred_width)

    def test_shredding(self):
        shreds = self.shred_maker.get_shreds(
            self.source_image, self.shred_width)

        self.assertEqual(len(shreds), 20, '20 shreds was expected')

        error_msg = 'shred did not match expected shred file %s'
        for shred, expected_shred in izip(shreds, self.expected_shreds):
            self.assertEqual(shred.tobytes(), expected_shred.tobytes(),
                             error_msg % expected_shred.filename)

    def test_assemble(self):
        assembled_image = self.shred_maker.assemble(self.expected_shreds)

        self.assertEqual(
            self.source_image.tobytes(), assembled_image.tobytes(),
            'Reassembled image does not match original image')
