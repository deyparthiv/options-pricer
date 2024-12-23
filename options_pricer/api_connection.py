import requests
import os 
from dotenv import load_dotenv

load_dotenv()
financial_modelling_prep_api_key = os.getenv("FINANCIAL_MODELLING_PREP_API_KEY")
"""returns a list of historical prices of a stock for the purposes of volatility calcultaion.
    The prices are the closing prices every day for the last five years. 
    Args:
        symbol (str): the symbol of the stock
    Returns:
        list: a list of historical prices of the stock
    Raises:
        Exception: error fetching data
"""
def get_historical_prices_of_stock(symbol:str) -> list:
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={financial_modelling_prep_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching historical prices for {symbol}")
    values = response.json()
    values = values['historical']
    historial_prices = []
    for value in values:
        historial_prices.append(value['close'])
    print("Succesfully fetched historical price for",symbol)
    return historial_prices
"""returns the spot price of a stock"""
def get_spotprice_of_stock(symbol:str) -> float:
    url = f"https://financialmodelingprep.com/api/v3/quote-short/{symbol}?apikey={financial_modelling_prep_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching spot price for {symbol}")
    value = response.json()
    print("Succesfully fetched spot price for",symbol)
    return value[0]['price']
"""returns the interest rate right now"""
def get_risk_free_interest_rate() -> float:
    return 4.52
