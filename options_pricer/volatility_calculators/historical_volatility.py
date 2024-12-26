from options_pricer.volatility_calculators import VolatilityCalculator
from options_pricer.assets.asset import Asset

class HistoricalVolatilityCalculator(VolatilityCalculator):
    def calculate_volatility(self, asset: Asset) -> float:
        pass