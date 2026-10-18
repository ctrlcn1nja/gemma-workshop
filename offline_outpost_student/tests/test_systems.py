"""Run: python -m unittest discover -s tests -v"""
import unittest
from systems.purifier import remaining_contamination
from systems.food_collector import HarvestRobot, station_total
from systems.radio import transmit_signal

class PurifierTests(unittest.TestCase):
    def test_two_filters(self):
        self.assertAlmostEqual(remaining_contamination(100, [0.6, 0.6]), 16)
    def test_no_filters(self):
        self.assertAlmostEqual(remaining_contamination(40, []), 40)
    def test_one_filter(self):
        self.assertAlmostEqual(remaining_contamination(100, [0.25]), 75)
    def test_complete_filter(self):
        self.assertAlmostEqual(remaining_contamination(80, [0.5, 1.0]), 0)

class FoodTests(unittest.TestCase):
    def test_independent_robots(self):
        a, b = HarvestRobot('A'), HarvestRobot('B')
        a.collect(5); b.collect(3)
        self.assertEqual((a.total(), b.total(), station_total([a,b])), (5,3,8))
    def test_empty_robot(self):
        self.assertEqual(HarvestRobot('Empty').total(), 0)
    def test_negative_harvest_rejected(self):
        with self.assertRaises(ValueError): HarvestRobot('A').collect(-1)

class RadioTests(unittest.TestCase):
    def test_acknowledgment_on_last_attempt(self):
        self.assertTrue(transmit_signal([False, False, True], 3))
    def test_acknowledgment_on_first_attempt(self):
        self.assertTrue(transmit_signal([True, False, False], 3))
    def test_no_acknowledgment(self):
        self.assertFalse(transmit_signal([False, False, False], 3))
    def test_acknowledgment_after_limit(self):
        self.assertFalse(transmit_signal([False, False, True], 2))

if __name__ == '__main__': unittest.main()
