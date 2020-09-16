import urllib.request,json
from .models import NewsSource, NewsArticle
import datetime#wanted to implement search article:later though

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['API_BASE_URL']
