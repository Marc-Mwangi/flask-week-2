import unittest
from models import news
News = news.News
class NewsTest(unittest.TestCase):
    """
    Tesr behavior of News class
    """
    def setUp(self):
        """
        method to run before every test
        """
        