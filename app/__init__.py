from flask import Flask

from app.config import DevConfig
from flask_bootstrap import Bootstrap



#Initialization
app = Flask(__name__)

#Setting up configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Flask Extensions

bootstrap = Bootstrap(app)

#Avoiding circular dependancy
from app import views