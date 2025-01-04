import datetime
from options_pricer.assets.asset import Asset

class Stock(Asset):
    """A class representing a stock."""
    def __init__(self, symbol: str, spot_price: float, volatility: float, interest_rate: float):
        self.__symbol = symbol
        self.__spot_price = spot_price
        self.__volatility = volatility
        self.__interest_rate = interest_rate
        self.__timeCreated = datetime.datetime.now()
        
    def get_symbol(self) -> str: return self.__symbol
    def get_spot_price(self) -> float: return self.__spot_price
    def get_volatility(self) -> float: return self.__volatility
    def get_interest_rate(self) -> float: return self.__interest_rate
