from app import app
from .request import api_key

@app.route('/')
def index():
    
    return 'Hello'