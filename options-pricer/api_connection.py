import requests
import os 
from dotenv import load_dotenv, dotenv_values

load_dotenv()

"""returns a list of historical prices of a stock for the purposes of volatility calcultaion.
    The prices are the closing prices every day for the last five years. 
    Args:
        symbol (str): the symbol of the stock
    Returns:
        list: a list of historical prices of the stock
    Raises:
        Exception: error fetching data
"""
def get_historical_price_of_stock(symbol:str) -> list:
    print(symbol)
    financial_modelling_prep_api_key : str= os.getenv("FINANCIAL_MODELLING_PREP_API_KEY")
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={financial_modelling_prep_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Error fetching data")
    values = response.json()
    values = values['historical']
    historial_prices = []
    for value in values:
        historial_prices.append(value['close'])
    return historial_prices
