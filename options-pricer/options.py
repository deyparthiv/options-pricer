import datetime
from abc import ABC,abstractmethod
from pricing_models import PriceCalculator
from assets import Asset

class Option(ABC):
    @abstractmethod
    def get_asset(self) -> Asset: pass
    @abstractmethod
    def get_strike_price(self) -> float: pass
    @abstractmethod
    def get_maturity_date(self) -> datetime: pass
    @abstractmethod
    def is_call(self) -> bool: pass
    @abstractmethod
    def get_time_to_maturity(self) -> float: pass
    @abstractmethod
    def accept(self, price_calculator:PriceCalculator) -> None: pass
    
class EuropeanOption(Option):
    def __init__(self, asset: Asset, strike_price: float, maturity_date: datetime, is_call: bool):
        self.__asset = asset
        self.__strike_price = strike_price
        self.__maturity_date = maturity_date
        self.__is_call = is_call
    
    def get_asset(self) -> Asset:
        return self.__asset
    def get_strike_price(self) -> float:
        return self.__strike_price
    def get_maturity_date(self) -> datetime:
        return self.__maturity_date
    def is_call(self) -> bool:
        return self.__is_call
    """Returns the time to maturity of the option in years"""
    def get_time_to_maturity(self):
        return (self.__maturity_date - datetime.datetime.now()).days / 365
    def accept(self, price_calculator:PriceCalculator) -> None:
        price_calculator.visit(self)
        




    