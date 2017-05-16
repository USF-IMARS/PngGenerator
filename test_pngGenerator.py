from unittest import TestCase
from PngGenerator import PngGenerator

__author__ = 'gabyq'


class TestPngGenerator(TestCase):

    def setUp(self):
        self.generator = PngGenerator(None,None, "data", None)
        self.generator.setCoordinates(55, -45, -5, -125)


    def test_getNewLimits(self):
        slin, spix, elin, epix = self.generator.getNewLimits(8800, 6600, 16.0, -58.0, 8.0, -77.0)
        new_width = epix - spix
        new_height = elin - slin

        self.assertEqual(new_width, 1985)
        self.assertEqual(new_height, 885)
        self.assertEqual(spix, 5281)
        self.assertEqual(epix, 7370)
        self.assertEqual(slin, 4291)
        self.assertEqual(elin, 5170)

    def test_getPixelResolution(self):
        constant = 1000000
        value1 = int(0.0090909 * constant)

        resolution = self.generator.getPixelResolution(55, -5, 6600)
        value2 = int(resolution * constant)
        self.assertEqual(value1, value2, "Error determining verical resolution Fullpass 0.00909 != " + str(resolution))

        resolution = self.generator.getPixelResolution(-45, -125, 8800)
        value2 = int(resolution * constant)
        self.assertEqual(value1, value2, "Error determining horizontal resolution Fullpass 0.00909 != " + str(resolution))

    def test_centerCoordinates(self):
        self.fail()