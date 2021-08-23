import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
APLHA_API_KEY = "XXXXXXXXXXXX"
url = 'https://www.alphavantage.co/query'


param = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "datatype": "json",
    "apikey": APLHA_API_KEY
}


def stock_chart():
    r = requests.get(url, params=param)
    r.raise_for_status()
    yestarday = date_finder(1)
    yestarday += " 19:00:00"
    today = date_finder(0)
    today += " 19:00:00"
    yesterday_price = find_price(r, yestarday)
    today_price = find_price(r, today)
    return (yesterday_price, today_price)


def find_price(r, date_var):
    return r.json()["Time Series (60min)"][date_var]["3. low"]


def date_finder(z=1):
    aux = 1
    if(dt.datetime.today().weekday()-z == 5):  # o mercado fecha o fim de semana
        aux = 2
    elif(dt.datetime.today().weekday()-z == 6):
        aux = 2
    elif(dt.datetime.today().weekday()-z <= 0):
        aux = 3
    aux += z
    day = dt.date.today() - dt.timedelta(days=aux)
    day = day.strftime("%Y-%m-%d")
    # print(day)
    return day
