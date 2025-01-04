from abc import ABC, abstractmethod

class Asset(ABC):
    """A class representing an asset."""
    @abstractmethod
    def get_symbol(self) -> str: pass
    @abstractmethod
    def get_spot_price(self) -> float: pass
    @abstractmethod
    def get_volatility(self) -> float: pass
    @abstractmethod
    def get_interest_rate(self) -> float: pass