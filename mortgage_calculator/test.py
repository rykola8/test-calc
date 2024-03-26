import unittest

from functions import calculate_monthly_payment

class TestMortgageCalculator(unittest.TestCase):

    def test_calculate_monthly_payment(self):
        # Test case 1: Monthly payment calculation
        self.assertAlmostEqual(calculate_monthly_payment(100000, 5, 30), 536.82, places=2)

unittest.main()