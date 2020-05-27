import mongoengine
from flask import Flask 
from mongoengine import *

class User(Document):
    username = StringField(required=True, max_length=30)
    email = StringField(required=True, max_length=50)
    password = StringField(required=True)