from flask import Flask
from flask_pymongo import PyMongo

app = Flask("didsys")
mongo = PyMongo(app)