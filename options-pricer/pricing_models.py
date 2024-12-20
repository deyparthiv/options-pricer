from abc import ABC,abstractmethod
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
        C = 
    def getPutPrice(self, option: EuropeanOption) -> float:
        pass
    
class BinomialPricingModel(PricingModel):
    def getPrice(self, option: Option) -> float:
        pass
    
class MonteCarloPricingModel(PricingModel):
    def getPrice(self, option: Option) -> float:
        pass

    
