from options_pricer.options.option import Option, EuropeanOption, AmericanOption
import numpy as np

class BinomialPricingModel():
    
    def get_price_european(self, option: EuropeanOption, steps: int) -> float:
        """Returns the price of a European option using the binomial pricing model."""
        if option.is_call:
            return self.__get_call_price_european(option, steps)
        else:
            raise NotImplementedError("Put options are not yet implemented")
        
    def get_price_american(self, options: AmericanOption) -> float:
        """Returns the price of an American option using the binomial pricing model."""
        raise NotImplementedError("American options are not yet implemented")
    
    def __get_call_price_european(self, option: EuropeanOption, steps: int) -> float:
        # constructs a binomial tree recursively and evaluates the value of the option at each node
        risk_free_interest = option.get_asset().get_interest_rate()
        strike_price = option.get_strike_price()
        S_0 = option.get_asset().get_spot_price()
        T = option.get_time_to_maturity()
        volatility = option.get_asset().get_volatility()
        dt = T/steps
        u = np.exp(volatility*np.sqrt(dt))
        d = 1/u
        price_to_val = {}
        return self.__helper_european_call(risk_free_interest,strike_price,S_0,u,d,dt,steps, price_to_val)
    
    def __call_option_payoff(self,S,K) -> float:
        return max(S-K,0)

    def __helper_european_call(self,risk_free_interest,strike_price,S_0,u,d,dt, step:int, price_to_val: dict):
        # recursively constructs a binomial tree and evaluates the value of the option at each node
        print("Branch:",S_0)
        if S_0 in price_to_val:
            return price_to_val[S_0]
        if step == 0:
            return self.__call_option_payoff(S_0,strike_price)
        else:
            up_val = self.__helper_european_call(risk_free_interest,strike_price,S_0*u,u,d,dt,step-1, price_to_val)
            price_to_val[S_0*u] = up_val
            down_val = self.__helper_european_call(risk_free_interest,strike_price,S_0*d,u,d,dt,step-1, price_to_val)
            price_to_val[S_0*d] = down_val

            p = (np.exp(risk_free_interest*dt) - d)/(u-d)
            value = np.exp(-risk_free_interest*dt)*(p*up_val + (1-p)*down_val)

            return value