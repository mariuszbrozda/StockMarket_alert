

import requests
import os
from os import environ
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import datetime as dt


NIO_STOCK = "NIO"
STOCK_NAME=  NIO_STOCK

# STOCK MARKET
stock_api = os.environ.get('STOCK_API')
stock_endpoint = os.environ.get('STOCK_ENDPOINT')

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': NIO_STOCK,
    'apikey': stock_api,

}

nio_stock_response = requests.get(url=stock_endpoint, params=stock_params)

oil_stock_response = requests.get(url=stock_endpoint, params=stock_params)

nio_data = nio_stock_response.json()["Time Series (Daily)"]

data = [ value for (key,value) in nio_data.items() ]
nio_yesterday_data = data[0]
nio_day_before_data = data[1]


price_diff = abs(float(nio_yesterday_data['4. close']) - float(nio_day_before_data['4. close']))

price_percentage_diff = (price_diff / float(nio_yesterday_data['4. close'])) * 100

price_rounded = round(price_percentage_diff, 2)

up_down = None
if abs(price_rounded) > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# GETTING DATA FROM NEWS API
news_api = os.environ.get('NEWS_API')
news_endpoint = os.environ.get('NEWS_ENDPOINT')

print(nio_data)
news_params = {
    'qInTitle': 'NIO',
    'published': nio_yesterday_data,
    'apikey': news_api,
    'language': 'en',


}
news_response = requests.get(url=news_endpoint, params=news_params)

nio_news = news_response.json()

articles = nio_news['articles']

three_articles = articles[:3]

formatted_articles = [f"{STOCK_NAME}: {up_down} {price_rounded} % \n \n Headline: {article['title']}. \n Brief: {article['description']} \n" for article in three_articles]


# SEND SMS MESSAGE WITH NEWS AND NIO STOCK PRICE INFO

twillio_account_sid = os.environ.get('TWILLIO_ACC_SID')
twillio_auth_token = os.environ.get('TWILLIO_TOKEN')

client = Client(twillio_account_sid, twillio_auth_token)

for article in formatted_articles:
    message = client.messages \
            .create(
                body=f"{article} \n ",
                from_= os.environ.get('TWILLIO_PHONE_NR'),
                to= os.environ.get('RECEIVER_NUMBER')
            )
print(message.sid)

