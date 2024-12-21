from abc import ABC, abstractmethod
import api_connection
import numpy 
import volatility_calculators

class Asset(ABC):
    @abstractmethod
    def get_spot_price(self) -> float: pass
    @abstractmethod
    def get_volatility(self) -> float: pass
    @abstractmethod
    def get_interest_rate(self) -> float: pass

# TO DO : add dividend yield
class Stock(Asset):
    def __init__(self, symbol: str):
        self.symbol = symbol
        
    def get_spot_price(self) -> float:
        return api_connection.get_spotprice_of_stock(self.symbol)
    def get_volatility(self) -> float:
        return volatility_calculators.SimpleVolatilityCalculator().calculate_volatility(self)
    def get_interest_rate(self) -> float:
        return api_connection.get_risk_free_interest_rate()