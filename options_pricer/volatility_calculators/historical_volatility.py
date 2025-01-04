import numpy as np
from options_pricer.volatility_calculators.volatility_calculator import VolatilityCalculator
from options_pricer.assets.asset import Asset
from options_pricer.api_connection import get_historical_prices_of_stock

class HistoricalVolatilityCalculator(VolatilityCalculator):
    """A class to calculate the historical volatility of an asset."""
    def calculate_volatility_symbol(self, symbol: str) -> float:
        historical_prices = get_historical_prices_of_stock(symbol)
        for i in range(len(historical_prices)-1):
                historical_prices[i] = np.log(historical_prices[i+1]) - np.log(historical_prices[i])
        historical_prices.pop(-1)
        volatility = np.std(historical_prices)*np.sqrt(252)
        print(f"Volatility of {symbol} is {volatility}")
        return volatility
    
    def calculate_volatility(self, asset: Asset) -> float:
        historical_prices = get_historical_prices_of_stock(asset.symbol)
        for i in range(len(historical_prices)-1):
            historical_prices[i] = np.log(historical_prices[i+1]) - np.log(historical_prices[i])
        historical_prices.pop(-1)
        volatility = np.std(historical_prices)*np.sqrt(252)
        print(f"Volatility of {asset.symbol} is {volatility}")
        return volatility