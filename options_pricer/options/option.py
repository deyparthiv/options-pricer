from abc import ABC,abstractmethod
from options_pricer.assets.asset import Asset
import datetime

class Option(ABC):
    """An abstract class to represent an option."""
    @abstractmethod
    def get_asset(self) -> Asset:
        """Returns the asset that the option is based on."""
    @abstractmethod
    def get_strike_price(self) -> float:
        """Returns the strike price of the option."""
    @abstractmethod
    def get_maturity_date(self) -> datetime.date:
        """Returns the maturity date of the option."""
    @abstractmethod
    def is_call(self) -> bool:
        """Returns True if the option is a call option, False if it is a put option."""
    @abstractmethod
    def get_time_to_maturity(self) -> float:
        """Returns the approximate number of trading days to maturity of the option in terms of trading years"""
    
class EuropeanOption(Option):
    """A class to represent a European option"""
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

    def get_time_to_maturity(self): #this approximation is more accurate the longer the time scale
        """Returns the approximate number of trading days to maturity of the option in terms of trading years"""
        return (self.__maturity_date.toordinal() - datetime.date.today().toordinal()-104) / 252
        
class AmericanOption(Option):
    """A class to represent an American option."""
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

    def get_time_to_maturity(self): #this approximation is more accurate the longer the time scale
        """Returns the approximate number of trading days to maturity of the option in terms of trading years"""
        return (self.__maturity_date.toordinal() - datetime.date.today().toordinal()-104) / 252
      