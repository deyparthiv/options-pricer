from abc import ABC, abstractmethod
from options_pricer.assets.asset import Asset

class VolatilityCalculator(ABC):
    @abstractmethod
    def calculate_volatility(self, asset: Asset) -> float: pass
    @abstractmethod
    def calculate_volatility_symbol(self, symbol: str) -> float: pass

