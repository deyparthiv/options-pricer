from abc import ABC,abstractmethod

import numpy as np
from options import Option, EuropeanOption
from scipy.stats import norm

class PricingModel(ABC):
    @abstractmethod
    def getPrice(self, option: Option) -> float: 
        pass

class BlackScholesPricingModel(PricingModel):
    def getPrice(self, option: EuropeanOption) -> float:
        if option.is_call:
            return self.getCallPrice(option)
        else:
            return self.getPutPrice(option)
    
    def getCallPrice(self, option: EuropeanOption) -> float:
            
        d1 = (np.log(option.get_strike_price() / option.strike_price) + (option.r + 0.5 * option.sigma ** 2) * option.T) / (option.sigma * np.sqrt(option.T))
        C = norm()
    def getPutPrice(self, option: EuropeanOption) -> float:
        pass
    
class BinomialPricingModel(PricingModel):
    def getPrice(self, option: Option) -> float:
        pass
    
class MonteCarloPricingModel(PricingModel):
    def getPrice(self, option: Option) -> float:
        pass

    
