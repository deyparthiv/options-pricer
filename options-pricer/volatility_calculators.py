from abc import ABC, abstractmethod
from assets import Asset
import api_connection
import numpy as np

class VolatilityCalculator(ABC):
    @abstractmethod
    def calculate_volatility(self, asset: Asset) -> float: pass
    
class SimpleVolatilityCalculator(VolatilityCalculator):
    def calculate_volatility(self, asset: Asset) -> float:
        """Returns the volatility of a stock based on the historical prices of the stock
        Args:
            asset (Asset): the asset whose volatility is to be calculated
        Returns: float: the standard derivation of the historical prices of the stock"""
        historical_prices = api_connection.get_historical_price_of_stock(asset.symbol)
        volalitity = np.std(historical_prices)
        return volalitity
    
class HistoricalVolatilityCalculator(VolatilityCalculator):
    def calculate_volatility(self, asset: Asset) -> float:
        pass
    
class ImpliedVolatilityCalculator(VolatilityCalculator):
    def calculate_volatility(self, asset: Asset) -> float:
        pass
    

