from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import NewsArticle

@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and interpolated data
    '''

   # Getting sources

    title = 'Home - Welcome to News411'
    source=get_sources()
    articles = request.args.get('source_name')
    if articles:
        return redirect(url_for('.source',sources=articles))
    else:
        return render_template('index.html', title = title, sources=source)
 # Getting articles
@main.route('/sources/articles/<source_name>')
def source(source_name):
    '''
    View source page function that returns the articles page and expressions delimitors
    '''

    title='Enjoy the articles'
    
    source=get_articles(source_name)
    return render_template('articles.html', title = title, sources=source)
© 2