from abc import ABC,abstractmethod
from options import Option, EuropeanOption

class PricingModel(ABC):
    def __innit__(self, ):
        
    @abstractmethod
    def getEuopeanOptionPrice(self, option: Option): pass

class BlackScholesPricingModel(PricingModel):
    
    
    def getPrice(self, option: EuropeanOption) -> float:
        if option.is_call:
            return self.getCallPrice(option)
        else:
            return self.getPutPrice(option)
    def getCallPrice(self, option: EuropeanOption) -> float:
        pass
    def getPutPrice(self, option: EuropeanOption) -> float:
        pass
    
    
class BinomialPricingModel(PricingModel):
    def getPrice(self, option: Option) -> float:
        pass
    
class MonteCarloPricingModel(PricingModel):
    def getPrice(self, option: Option) -> float:
        pass

    
