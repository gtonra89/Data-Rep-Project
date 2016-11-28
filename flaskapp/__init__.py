from flask import Flask

flaskapp = Flask(__name__)
flaskapp.config["SECRET_KEY"] = "abc123babyyouandme"

from flaskapp import View

