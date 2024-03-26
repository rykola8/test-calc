import unittest

from functions import calculate_calories_burned

class TestCaloriesBurnedCalculator(unittest.TestCase):

    def test_calculate_calories_burned_running(self):
        self.assertEqual(calculate_calories_burned("running", 30, 70), 350)

    def test_calculate_calories_burned_invalid_activity(self):
        self.assertEqual(calculate_calories_burned("walking", 60, 75), "Activity not found. Please choose from: running, cycling, swimming")

unittest.main()