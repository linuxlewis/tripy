import unittest

from ddt import ddt, data, unpack
import tripy


STAR = [(350, 75), (379, 161), (469, 161), (397, 215), (423, 301), (350, 250), (277, 301), (303, 215), (231, 161), (321, 161)]
STAR_TRIANGLES = [((321, 161), (350, 75), (379, 161)), ((379, 161), (469, 161), (397, 215)), ((379, 161), (397, 215), (423, 301)), ((379, 161), (423, 301), (350, 250)), ((379, 161), (350, 250), (277, 301)), ((379, 161), (277, 301), (303, 215)), ((303, 215), (231, 161), (321, 161)), ((321, 161), (379, 161), (303, 215))]
SIMPLE_DIAMOND = [(0,1), (-1, 0), (0, -1), (1, 0)]
SIMPLE_DIAMOND_TRIANGLES = [((1, 0), (0, 1), (-1, 0)), ((1, 0), (-1, 0), (0, -1))]
NO_CONVEX_VERTEX = [(-2.0, -17.0), (-2.0, -8.0), (-8.0, -2.0), (-17.0, -2.0), (-20.0, -8.0), (-18.0, -17.0), (-12.0, -24.0), (-7.0, -22.0)]
NO_CONVEX_VERTEX_TRIANGLES = [((-2.0, -17.0), (-7.0, -22.0), (-12.0, -24.0)), ((-2.0, -17.0), (-12.0, -24.0), (-18.0, -17.0)), ((-2.0, -17.0), (-18.0, -17.0), (-20.0, -8.0)), ((-2.0, -17.0), (-20.0, -8.0), (-17.0, -2.0)), ((-2.0, -17.0), (-17.0, -2.0), (-8.0, -2.0)), ((-2.0, -17.0), (-8.0, -2.0), (-2.0, -8.0))]

TEST_DATA = [
    (STAR, STAR_TRIANGLES),
    (SIMPLE_DIAMOND, SIMPLE_DIAMOND_TRIANGLES),
    (NO_CONVEX_VERTEX, NO_CONVEX_VERTEX_TRIANGLES)
]


@ddt
class TestPolygons(unittest.TestCase):

    @data(*TEST_DATA)
    @unpack
    def test_polygon(self, polygon, expected):
        actual = tripy.earclip(polygon)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
