import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class SimpleMongoDBReadTest(unittest.TestCase):
    def setUp(self):
        # Connect to MongoDB using the details from the .env file
        self.client = MongoClient(f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_CLUSTER')}/?retryWrites=true&w=majority")

    def test_ping_mongodb(self):
        # Try pinging MongoDB to check if it’s working
        try:
            self.client.admin.command('ping')  # Send a ping to the database
            connection_status = True  # If no errors, it's connected
        except Exception:
            connection_status = False  # If there’s an error, it’s not connected

        # Check if the ping worked (i.e., connection is alive)
        self.assertTrue(connection_status)

if __name__ == '__main__':
    unittest.main()  # Run the test
