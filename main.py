

import pandas
import requests
import os
from os import environ
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

NIO_STOCK = "NIO"
OIL_STOCK = 'OIL'
BERKSHIRE = 'BRK.B'
COMPANY_NAME = "Tesla Inc"

# STOCK MARKET
alphavantage_api = os.environ.get('STOCK_API')
stock_endpoint = os.environ.get('STOCK_ENDPOINT')

stock_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': NIO_STOCK,
    'interval': '60min',
    'apikey': alphavantage_api,

}

nio_stock_response = requests.get(url=stock_endpoint, params=stock_params)

oil_stock_response = requests.get(url=stock_endpoint, params=stock_params)
print(nio_stock_response.json())



twillio_account_sid = os.environ.get('ACC_SID')
twillio_auth_token = os.environ.get('TWILLIO_AUTH_TOKEN')


client = Client(twillio_auth_token, twillio_account_sid)

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}


client = Client(twillio_account_sid, twillio_auth_token, http_client=proxy_client)
message = client.messages \
        .create(
        body='messge',
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
print(message.status)

