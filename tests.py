import unittest
from SegmentIntersection import find_orientation, on_segment, do_intersect

class TestIntersect(unittest.TestCase):
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
    
    def test_on_segment_true(self):
        self.assertEqual(on_segment((0,0), (1,1), (2,2)), True)

    def test_on_segment_false(self):
        self.assertEqual(on_segment((0,0), (2,2), (1,1)), False)

    def test_on_segment_fail(self):
        self.assertEqual(on_segment((), (1,1), (2,2)), -1)
    
    def test_intersect(self):
        self.assertEqual(do_intersect(((1, 1), (4, 4)), ((2, 4), (4,2))), True)

    def test_intersect_wrong(self):
        self.assertEqual(do_intersect(((1, 1), (4, 4)), ((1, -1), (2,-4))), False)

    def test_intersect_collinear(self):
        self.assertEqual(do_intersect(((0, 0), (1, 1)), ((1, 1), (2, 2))), True)
    
    def test_intersect_collinear_wrong(self):
        self.assertEqual(do_intersect(((0, 0), (1, 1)), ((2, 2), (3, 3))), False)
    
    def test_intersect_bad_input(self):
        self.assertEqual(do_intersect((),()), -1)

if __name__ == "__main__":
    unittest.main()