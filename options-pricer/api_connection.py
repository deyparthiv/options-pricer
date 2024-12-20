import requests
import os 
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def get_historical_price_of_stock(symbol:str):
    print(symbol)
    financial_modelling_prep_api_key : str= os.getenv("FINANCIAL_MODELLING_PREP_API_KEY")
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={financial_modelling_prep_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Error fetching data")
    return response.json()