from abc import ABC, abstractmethod
from assets import Asset

class VolatilityCalculator(ABC):
    @abstractmethod
    def calculate_volatility(self, asset: Asset) -> float: pass
    
class HistoricalVolatilityCalculator(VolatilityCalculator):
    def calculate_volatility(self, asset: Asset) -> float:
        pass
    
class ImpliedVolatilityCalculator(VolatilityCalculator):
    def calculate_volatility(self, asset: Asset) -> float:
        pass
    

