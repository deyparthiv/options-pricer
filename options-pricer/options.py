import datetime
from abc import ABC,abstractmethod
from pricing_models import PriceCalculator

class Option(ABC):
    @abstractmethod
    def get_strike_price(self) -> float: pass
    @abstractmethod
    def get_maturity_date(self) -> datetime: pass
    @abstractmethod
    def is_call(self) -> bool: pass
    @abstractmethod
    def accept(self, price_calculator:PriceCalculator) -> None: pass
    
class EuropeanOption:
    def __init__(self, strike_price: float, maturity_date: datetime, is_call: bool):
        self.strike_price = strike_price
        self.maturity_date = maturity_date
        self.is_call = is_call
    
    def get_strike_price(self) -> float:
        return self.strike_price
    def get_maturity_date(self) -> datetime:
        return self.maturity_date
    def is_call(self) -> bool:
        return self.is_call
    def accept(self, price_calculator:PriceCalculator) -> None:
        price_calculator.visit(self)
        




    