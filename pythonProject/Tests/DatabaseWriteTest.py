import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class SimpleMongoDBWriteTest(unittest.TestCase):
    def setUp(self):
        # Connect to MongoDB using the connection string
        self.client = MongoClient(f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_CLUSTER')}/?retryWrites=true&w=majority")
        self.db = self.client["app"]
        self.collection = self.db["products"]

    def test_insert_document(self):
        # Create a new product to insert into the database
        new_product = {
            "name": "Simple Test Product",  # Product name
            "tag": "new",  # Tag (like "new", "sale", etc.)
            "price": 29.99,  # Price of the product
            "image_path": "/static/images/test_product.jpg"  # Image path (or URL)
        }

        # Insert the new product into the database
        self.collection.insert_one(new_product)

        inserted_product = self.collection.find_one({"name": "Simple Test Product"})

        # Make sure the product is there (check if it's not None)
        self.assertIsNotNone(inserted_product)
        # Also check if the name is correct
        self.assertEqual(inserted_product["name"], "Simple Test Product")

    def tearDown(self):
        self.collection.delete_one({"name": "Simple Test Product"})

if __name__ == '__main__':
    unittest.main()  # Run the test