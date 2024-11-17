import unittest
from app import app

class SimpleRouteTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Set up the Flask test client
        self.app.testing = True  # Make sure Flask is in testing mode

    def test_invalid_method_on_products_route(self):
        # Try sending a POST request to /products (but it should only accept GET)
        response = self.app.post('/products')

        # Check if it gives us a 405 status code (Method Not Allowed)
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()  # Run the test