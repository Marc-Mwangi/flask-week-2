from app import app
import urllib.request,json
from .models import news

News = news.News

key= app.config['news_api_key']

base_url = app.config['news_api_base']

def report(category):
    full_url= base_url.format(category,key)
    with urllib.request.urlopen(report) as url:
        report_data= url.read()
        report_response= json.loads(report_data)

        report_results= None

        if report_response['results']:
            report_list = report_response['results']
            report_result = process_results(report_list)
    return report_results