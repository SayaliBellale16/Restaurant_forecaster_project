import unittest
from app import app

class APITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_add_order(self):
        res = self.client.post('/add_order', json={
            "customers": 10,
            "hour": 12
        })
        self.assertEqual(res.status_code, 200)

    def test_forecast(self):
        res = self.client.get('/forecast')
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()