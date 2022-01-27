class Config:
    '''
    class defining objects used both in development and production
    '''
    news_api_base = 'https://newsapi.org/v2/everything?q=keyword&apiKey={}'
    news_api_key = '1bb43ee956f64da3acfc75c662b86430'
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG =True
