from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_CLUSTER = os.getenv('MONGODB_CLUSTER')

client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}/?retryWrites=true&w=majority")

# Original database
db = client["app"]
products_collection = db["products"]

# New database for a separate set of data
db_v2 = client["app_v2"]
products_collection_v2 = db_v2["products"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    products = list(products_collection.find())
    return render_template("products.html", products=products)

@app.route("/products_v2")
def products_v2():
    products_v2 = list(products_collection_v2.find())
    return render_template("products.html", products=products_v2)

app.run(host="0.0.0.0", port=5000)