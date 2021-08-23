from newsapi import NewsApiClient
from stockz import date_finder
import random


def get_news_TSLA():
    newsapi = NewsApiClient(api_key='XXXXXXXXXXXXXXXXXX')

    top_headlines = newsapi.get_top_headlines(q='tesla',
                                              category='business',
                                              language='en')

    title_article = top_headlines["articles"][0]["title"]
    brief_article = top_headlines["articles"][0]["description"]
    return (title_article, brief_article)
