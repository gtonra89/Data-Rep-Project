#create a Flask instance in __init__.py
from flask import Flask
flaskapp = Flask(__name__) 

flaskapp.config["SECRET_KEY"] = "abc123babyyouandme" #configure secret key value

from flaskapp import View #import the view 

