from abc import ABC,abstractmethod

class PricingModel(ABC):
    @abstractmethod
    def getPrice(): pass
