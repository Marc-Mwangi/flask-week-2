from flask import Flask

#Initialization
app = Flask(__name__)

#Setting up configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Avoiding circular dependancy
from app import views