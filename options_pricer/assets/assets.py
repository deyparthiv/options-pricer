from abc import ABC, abstractmethod
import api_connection
import numpy 
import volatility_calculators

class Asset(ABC):
    @abstractmethod
    def get_symbol(self) -> str: pass
    @abstractmethod
    def get_spot_price(self) -> float: pass
    @abstractmethod
    def get_volatility(self) -> float: pass
    @abstractmethod
    def get_interest_rate(self) -> float: pass

class Stock(Asset):
    def __init__(self, symbol: str, spot_price: float, volatility: float, interest_rate: float):
        self.__symbol = symbol
        self.__spot_price = spot_price
        self.__volatility = volatility
        self.__interest_rate = interest_rate
    def get_symbol(self) -> str: return self.__symbol
    def get_updated_spot_price(self) -> float:
        return api_connection.get_spotprice_of_stock(self.symbol)
    def get_updated_volatility(self) -> float:
        return volatility_calculators.SimpleVolatilityCalculator().calculate_volatility(self)
    def get_updated_interest_rate(self) -> float:
        return api_connection.get_risk_free_interest_rate()
    def get_spot_price(self) -> float: return self.__spot_price
    def get_volatility(self) -> float: return self.__volatility
    def get_interest_rate(self) -> float: return self.__interest_rate
