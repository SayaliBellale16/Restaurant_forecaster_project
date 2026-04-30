import unittest
from forecast import total_customers

class ForecastTest(unittest.TestCase):

    def test_total(self):
        hourly = {0: 10, 1: 20}
        self.assertEqual(total_customers(hourly), 30)

if __name__ == "__main__":
    unittest.main()