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
def get_sources():
    '''
    Function gets the json response to url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)


    return sources_results

def process_sources_results(sources_list):
    '''
    Function  processes  sources result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns :
        sources_results: A list of newssources objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        
              
        sources_object = NewsSource(id,name,description,url)
        sources_results.append(sources_object)

    return sources_results

def get_articles(source_name):
    search_movie_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source_name,api_key)
    with urllib.request.urlopen(search_movie_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_articles_data)

        search_articles_results = None

        if search_articles_response['articles']:
            search_articles_list = search_articles_response['articles']
            search_articles_results = process_articles_results(search_articles_list)

    return search_articles_results

def process_articles_results(articles_list):
    '''
    Function  processes  articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        articles_results: A list of newssources objects
    '''
    articles_results = []
    for item in articles_list:
        name = item.get('source')
        author=item.get("author")
        title=item.get("title")
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt= item.get("publishedAt")  

        articles_object = NewsArticle(name,author,title, description, url, urlToImage, publishedAt)
        articles_results.append(articles_object)

    return articles_results
