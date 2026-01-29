import unittest
from src.domain.value_objects.drawdown import Drawdown

class TestDrawdown(unittest.TestCase):
    def test_valid_drawdown(self):
        d = Drawdown(-15.0)
        self.assertEqual(d.value, -15.0)

    def test_zero_drawdown(self):
        d = Drawdown(0.0)
        self.assertEqual(d.value, 0.0)

    def test_positive_drawdown_raises_error(self):
        with self.assertRaises(ValueError):
            Drawdown(5.0)

if __name__ == '__main__':
    unittest.main()
