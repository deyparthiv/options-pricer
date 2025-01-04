from options_pricer.options.option import Option

class MonteCarloPricingModel():
    def getPrice(self, option: Option) -> float:
        raise NotImplementedError("Monte Carlo pricing is not yet implemented")
