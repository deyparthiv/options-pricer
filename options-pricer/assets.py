from abc import ABC, abstractmethod

class Asset(ABC):
    @abstractmethod
    def get_price(self) -> float: pass
    @abstractmethod
    def get_volatility(self) -> float: pass
    @abstractmethod
    def get_interest_rate(self) -> float: pass

class Stock(Asset):
    def __init__(self, price: float, volatility: float, interest_rate: float):
        self.price = price
        self.volatility = volatility
        self.interest_rate = interest_rate
    def get_price(self) -> float:
        return self.price
    def get_volatility(self) -> float:
        return self.volatility
    def get_interest_rate(self) -> float:
        return self.interest_rate