from app import app
from .request import api_key, base_url
import requests ,json
from flask import render_template

@app.route('/')
def index():
    news_url= base_url+api_key
    articles= requests.get(news_url)
    report= json.loads(articles.content)
    final= report['articles']
    publish = final[0]
    length = len(final)
    m=[]
    for i in range(0,length):
            if final[i]['source']['name'] not in m:
                m.append(final[i]['source']['name'])
    v = m
    l= len(v)
    return render_template('index.html', data= final ,report =report, outlet= publish, v=v, l=l, length = length)

@app.route('/outlet/<source>')
def outlet(source):
    news_url= base_url+api_key
    articles= requests.get(news_url)
    report= json.loads(articles.content)
    final= report['articles']
    publish = final[0]
    length = len(final)
    r=[]
    for i in range(0,length):
        if source == final[i]['source']['name']:
            r.append(final[i])
            print(r)

    m=[]
    for i in range(0,length):
            if final[i]['source']['name'] not in m:
                m.append(final[i]['source']['name'])
    v = m
    l= len(v)
    ld =len(r)
    return render_template('source.html', data =r , v=v, l=l, length = length, report =report, outlet= publish ,ld=ld)