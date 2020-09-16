class NewsSource:
    '''
    NewsSource class to define Source Objects
    '''

    def __init__(self,id,name,description,url):
        self.id =id
        self.name=name
        self.description=description
        self.url = url



class NewsArticle:
    '''
    NewsArticle class to define article Objects
    '''

    def __init__(self, name, author, title, description, url, urlToImage, publishedAt):
        self.name=name
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt