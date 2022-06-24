

import pandas
import requests
import os
from os import environ
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import datetime as dt



NIO_STOCK = "NIO"
OIL_STOCK = 'OIL'
BERKSHIRE = 'BRK.B'
COMPANY_NAME = "Tesla Inc"


STOCK_NAME=[NIO_STOCK, OIL_STOCK, BERKSHIRE ]

# STOCK MARKET
stock_api = ""
stock_endpoint = "https://www.alphavantage.co/query"



stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME[0],
    # 'interval': '60min',
    'apikey': stock_api,

}

nio_stock_response = requests.get(url=stock_endpoint, params=stock_params)

oil_stock_response = requests.get(url=stock_endpoint, params=stock_params)

nio_data = nio_stock_response.json()["Time Series (Daily)"]


data = [ value for (key,value) in nio_data.items() ]

nio_yesterday_data = data[0]
nio_day_before_data = data[1]

print(data)
print(nio_yesterday_data['4. close'])
print(nio_day_before_data['4. close'])

price_diff = abs(float(nio_yesterday_data['4. close']) - float(nio_day_before_data['4. close']))

price_percentage_diff = (price_diff / float(nio_yesterday_data['4. close'])) * 100

price_rounded = round(price_percentage_diff, 2)
print(price_rounded)


up_down = None
if price_rounded > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# GETTING DATA FROM NEWS API
news_api =''
news_endpoint = 'https://newsapi.org/v2/everything'

print(nio_data)
news_params = {
    'q': 'NIO STOCK',
    'published': nio_yesterday_data,
    'apikey': news_api,
    'language': 'en',


}
news_response = requests.get(url=news_endpoint, params=news_params)

nio_news = news_response.json()

articles = nio_news['articles']

three_articles = articles[:3]
print(three_articles)

formatted_articles = [f"{STOCK_NAME}: {up_down}{price_rounded}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)



#
# twillio_account_sid = ""
#
# twillio_auth_token = ""
#
#
#
# client = Client(twillio_account_sid, twillio_auth_token)
# nio_art_description = articles[:]['description']
# message_body = f''
# message = client.messages \
#         .create(
#             body=f"STOCK NEWS! {nio_art_description} \n ",
#             from_='',
#             to=''
#         )
# print(message.sid)

