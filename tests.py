import unittest
from SegmentIntersection import find_orientation

class TestOrientation(unittest.TestCase):
    def test_clockwise(self):
        self.assertEqual(find_orientation((0,0), (1,1), (2, 1)), 1)

    def test_counter_clockwise(self):
        self.assertEqual(find_orientation((0,0), (1,1), (1, 2)), 2)

    def test_collinear(self):
        self.assertEqual(find_orientation((0, 0), (1, 1), (2, 2)), 0)

    def test_weird(self):
        self.assertEqual(find_orientation((1, 1), (0,0), (2, 1)), 2)
    
    def test_wierd_collinear(self):
        self.assertEqual(find_orientation((1, 1), (0, 0), (2, 2)), 0)
    
    def test_missing_input(self):
        self.assertEqual(find_orientation((), (1, 1), (2, 2)), -1)
    
    def test_missing_input2(self):
        self.assertEqual(find_orientation((0, 0), (), (2, 2)), -1)
    
    def test_missing_input3(self):
        self.assertEqual(find_orientation((0, 0), (1, 1), ()), -1)

if __name__ == "__main__":
    unittest.main()