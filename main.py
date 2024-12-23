from options_pricer.assets.stock import Stock
from options_pricer.options.option import EuropeanOption 
import options_pricer.api_connection as api
from datetime import date
from options_pricer.pricing_models.black_scholes import BlackScholesPricingModel
import options_pricer.volatility_calculators.simple_volatility as simple_volatility

symbol = "AAPL"
spot_price = api.get_spotprice_of_stock(symbol)
volatility_calculator = simple_volatility.SimpleVolatilityCalculator()
volatility = volatility_calculator.calculate_volatility_symbol(symbol)
risk_free_rate = api.get_risk_free_interest_rate()
maturity_date = date.fromisoformat("2026-01-01")
asset = Stock("AAPL", spot_price, volatility, risk_free_rate)
option1 = EuropeanOption(asset, spot_price+10,maturity_date, True)

black_schools_model = BlackScholesPricingModel()
price = black_schools_model.getPrice(option1)
print(price)



