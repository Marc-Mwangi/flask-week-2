from app import app
from .request import api_key, base_url
import requests
from flask import render_template

@app.route('/')
def index():
    news_url= base_url+api_key
    articles= requests.get(news_url)
    report= articles.content
    return render_template('index.html', data= report)