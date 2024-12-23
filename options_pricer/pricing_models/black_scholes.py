from options_pricer.options.option import EuropeanOption
import numpy as np
from scipy.stats import norm

class BlackScholesPricingModel:
    def getPrice(self, option: EuropeanOption) -> float:
        if option.is_call:
            return self.getCallPrice(option)
        else:
            return self.getPutPrice(option)
    
    def getCallPrice(self, option: EuropeanOption) -> float:
        #varibles for the black scholes formula
        spot_price = option.get_asset().get_spot_price()
        risk_free_rate = option.get_asset().get_interest_rate()
        volatiliy = option.get_asset().get_volatility() 
        time_to_maturity = option.get_time_to_maturity() #in years
        strike_price = option.get_strike_price()
       
        d1 = (np.log(spot_price / strike_price) + (risk_free_rate + 0.5 * volatiliy ** 2) * time_to_maturity) / (volatiliy* np.sqrt(time_to_maturity))
        d2 = d1 - volatiliy * np.sqrt(time_to_maturity)
        
        C = norm.cdf(d1) * spot_price - norm.cdf(d2) * strike_price * np.exp(-1*risk_free_rate * time_to_maturity)
        return C
    
    def getPutPrice(self, option: EuropeanOption) -> float:
        #varibles for the black scholes formula
        spot_price = option.get_asset().get_spot_price()
        risk_free_rate = option.get_asset().get_interest_rate()
        volatiliy = option.get_asset().get_volatility() 
        time_to_maturity = option.get_time_to_maturity()
        strike_price = option.get_strike_price()
        
        d1 = (np.log(spot_price / strike_price) + (risk_free_rate + 0.5 * volatiliy ** 2) * time_to_maturity) / (volatiliy* np.sqrt(time_to_maturity))
        d2 = d1 - volatiliy * np.sqrt(time_to_maturity)
        
        P = strike_price * np.exp(-risk_free_rate * time_to_maturity) * norm.cdf(-d2) - spot_price * norm.cdf(-d1)
        return P