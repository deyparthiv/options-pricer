from datetime import date
import os
import requests
from dotenv import load_dotenv


load_dotenv() #load the environment variables from the .env file
financial_modelling_prep_api_key = os.getenv("FINANCIAL_MODELLING_PREP_API_KEY")

def get_historical_prices_of_stock_from_date(symbol:str, start_date: date) -> list:
    """Returns the historical end of day prices of a stock from a given date."""
    date_string= start_date.strftime("%Y-%m-%d")
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?from={date_string}?apikey={financial_modelling_prep_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.RequestException(f"Error fetching historical prices for {symbol}")
    values = response.json()
    values = values['historical']
    historial_prices = []
    for value in values:
        historial_prices.append(value['close'])
    print("Succesfully fetched historical price for",symbol)
    return historial_prices

def get_historical_prices_of_stock(symbol:str) -> list:
    """Returns the historical end of day prices of a stock from the last 5 years."""
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={financial_modelling_prep_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.RequestException(f"Error fetching historical prices for {symbol}")
    values = response.json()
    values = values['historical']
    historial_prices = []
    for value in values:
        historial_prices.append(value['close'])
    print("Succesfully fetched historical price for",symbol)
    return historial_prices

def get_spotprice_of_stock(symbol:str) -> float:
    """Returns the spot price of a stock."""
    url = f"https://financialmodelingprep.com/api/v3/quote-short/{symbol}?apikey={financial_modelling_prep_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.RequestException(f"Error fetching spot price for {symbol}")
    value = response.json()
    print("Succesfully fetched spot price for",symbol)
    return value[0]['price']

