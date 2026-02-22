import unittest
from src.domain.value_objects.contribution_amount import ContributionAmount

class TestContributionAmount(unittest.TestCase):
    def test_multiplication(self):
        amount = ContributionAmount(100.0)
        result = amount * 1.5
        self.assertEqual(result.value, 150.0)
        self.assertIsInstance(result, ContributionAmount)

    def test_multiplication_with_int(self):
        amount = ContributionAmount(100.0)
        result = amount * 2
        self.assertEqual(result.value, 200.0)

    def test_multiplication_rounding(self):
        amount = ContributionAmount(100.0)
        result = amount * 0.33333
        self.assertEqual(result.value, 33.33)

    def test_addition(self):
        amount1 = ContributionAmount(100.0)
        amount2 = ContributionAmount(50.0)
        result = amount1 + amount2
        self.assertEqual(result.value, 150.0)
        self.assertIsInstance(result, ContributionAmount)

    def test_negative_value_raises_error(self):
        with self.assertRaises(ValueError):
            ContributionAmount(-10.0)

if __name__ == '__main__':
    unittest.main()
