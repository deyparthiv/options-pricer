from abc import ABC,abstractmethod
from options_pricer.assets.asset import Asset
import datetime

class Option(ABC): #to represent the information about an option
    @abstractmethod
    def get_asset(self) -> Asset: pass
    @abstractmethod
    def get_strike_price(self) -> float: pass
    @abstractmethod
    def get_maturity_date(self) -> datetime.date: pass
    @abstractmethod
    def is_call(self) -> bool: pass
    @abstractmethod
    def get_time_to_maturity(self) -> float: pass
    
class EuropeanOption(Option):
    def __init__(self, asset: Asset, strike_price: float, maturity_date: datetime.date, is_call: bool):
        self.__asset = asset
        self.__strike_price = strike_price
        self.__maturity_date = maturity_date
        self.__is_call = is_call
        self.__creationTime = datetime.datetime.now()
    
    def get_asset(self) -> Asset:
        return self.__asset
    def get_strike_price(self) -> float:
        return self.__strike_price
    def get_maturity_date(self) -> datetime.date:
        return self.__maturity_date
    def is_call(self) -> bool:
        return self.__is_call
    """Returns the approximate number of trading days to maturity of the option in terms of trading years"""
    def get_time_to_maturity(self): #this approximation is more accurate the longer the time scale
        return (self.__maturity_date.toordinal() - datetime.date.today().toordinal()-104) / 252
        




    