from pricing_models import PricingModel
from options import Option

class MonteCarloPricingModel(PricingModel):
    def getPrice(self, option: Option) -> float:
        pass
