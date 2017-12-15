#!python3

import PricerConstants as cst
import  Stock

class Option:

    def __init__(self, underlying=None, type=cst.CALL, strike=100.00, spot=100.00, volat = 0.05, maturite=1, risk_free_fate=0.02,  market_price=100.00, feature='NONE', feature_val = 0.00):

        try:
            self.underlying = underlying
            self.type = type.upper()
            self.strike = strike
            self.spot = spot
            self.volat = volat
            self.maturite = maturite
            self.market_price = market_price
            self.risk_free_rate = risk_free_fate
            self.feature = feature
            self.barrier = 0.00
            self.asian_days = 0

            if self.spot != self.underlying.price or self.volat != self.underlying.sigma:
                self.underlying = Stock.Stock('TOTAL', 100.00, 0.02)
                self.spot = self.underlying.price
                self.volat = self.underlying.sigma

            if self.underlying is None or not isinstance(self.underlying, Stock.Stock):
                self.underlying = Stock.Stock('TOTAL', 100.00, 0.02)
                self.spot = self.underlying.price
                self.volat = self.underlying.sigma
            else:
                self.underlying = underlying
                self.spot = self.underlying.price
                self.volat = self.underlying.sigma

            if self.feature == cst.VANILLA:
                pass
            elif self.feature == cst.BARRIER:
                if feature_val == 0.00:
                    self.barrier = 0.7 * self.strike
                else:
                    self.barrier = feature_val/100 * self.strike
            elif self.feature == cst.ASIAN:
                if feature_val == 0.00:
                    self.asian_days = 30
                else:
                    self.asian_days = feature_val

        except:
            self.underlying = Stock.Stock('TOTAL', 100.00, 0.02)
            self.type = type.upper()
            self.strike = strike
            self.spot = spot
            self.volat = volat
            self.maturite = maturite
            self.market_price = market_price
            self.risk_free_rate = risk_free_fate
            self.feature = feature

            if self.feature == cst.VANILLA:
                pass
            elif self.feature == cst.BARRIER:
                if feature_val == 0.00:
                    self.barrier = 0.7 * self.strike
                else:
                    self.barrier = feature_val
            elif self.feature == cst.ASIAN:
                if feature_val == 0.00:
                    self.asian_days = 30
                else:
                    self.barrier = feature_val










