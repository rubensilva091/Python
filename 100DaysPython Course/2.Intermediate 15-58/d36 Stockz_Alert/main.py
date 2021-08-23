import requests
import stockz
import news
import twilio_p as tw
import datetime as dt


(title_article, brief_article) = news.get_news_TSLA()
(yesterday_value, today_value) = stockz.stock_chart()
value = (float(today_value) / float(yesterday_value))-1
if (value > .1):
    string = str((int(value*100)))
    tw.send_sms(title_article, brief_article, string)

