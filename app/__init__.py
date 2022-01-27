from flask import Flask

from app.config import DevConfig

#Initialization
app = Flask(__name__)

#Setting up configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Avoiding circular dependancy
from app import views