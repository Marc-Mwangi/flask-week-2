from app import app
import urllib.request,json
from .models import news

News = news.News
api_key='1bb43ee956f64da3acfc75c662b86430'
base_url ='https://newsapi.org/v2/everything?q=keyword&apiKey='

news_url= base_url.format(api_key)
print(news_url)
