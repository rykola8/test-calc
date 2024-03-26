import unittest
from bmi_calculator import calculate_bmi, interpret_bmi

class TestBMICalculator(unittest.TestCase):

    def test_calculate_bmi(self):
        # Test case 1: Normal BMI
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

        # Test case 2: Underweight BMI
        self.assertAlmostEqual(calculate_bmi(50, 1.75), 16.33, places=2)

        # Test case 3: Overweight BMI
        self.assertAlmostEqual(calculate_bmi(90, 1.75), 29.39, places=2)

        # Test case 4: Obese BMI
        self.assertAlmostEqual(calculate_bmi(100, 1.75), 32.65, places=2)

    def test_interpret_bmi(self):
        # Test case 1: Normal BMI
        self.assertEqual(interpret_bmi(22.86), "Normal weight")

        # Test case 2: Underweight BMI
        self.assertEqual(interpret_bmi(16.33), "Underweight")

        # Test case 3: Overweight BMI
        self.assertEqual(interpret_bmi(29.39), "Overweight")

        # Test case 4: Obese BMI
        self.assertEqual(interpret_bmi(32.65), "Obese")

if __name__ == "__main__":
    unittest.main()