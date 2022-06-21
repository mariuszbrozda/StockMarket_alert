

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
alphavantage_api =''
stock_endpoint = ''

stock_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': NIO_STOCK,
    'interval': '60min',
    'apikey': alphavantage_api,

}

nio_stock_response = requests.get(url=stock_endpoint, params=stock_params)

oil_stock_response = requests.get(url=stock_endpoint, params=stock_params)
print(nio_stock_response.json())




