import Pricer
from PricerIface import *
import unittest

class TestPricer(unittest.TestCase):

    def setUp(self):
        self.strike = 100
        self.spot = 100
        self.mat = 1
        self.rf = 0.02
        self.volat = 0.05


        self.myVanillaCallPricer = Pricer.OptionPricer('call', self.strike, self.spot, self.mat
                                                       , self.rf, self.volat, "EUR")
        self.myVanillaPutPricer = Pricer.OptionPricer('put', self.strike, self.spot, self.mat,
                                                      self.rf, self.volat, "EUR")

        self.myBarrierCallPricer = Pricer.OptionPricer('call',  self.strike, self.spot, self.mat,
                                                       self.rf, self.volat, "EUR", cst.BARRIER, 85)
        self.myBarrierPutPricer = Pricer.OptionPricer('put',  self.strike, self.spot, self.mat,
                                                      self.rf, self.volat, "EUR", cst.BARRIER, 85)

        self.myAsianCallPricer = Pricer.OptionPricer('call',  self.strike, self.spot, self.mat,
                                                     self.rf, self.volat, "EUR", cst.ASIAN, 30)
        self.myAsianPutPricer = Pricer.OptionPricer('put',  self.strike, self.spot, self.mat,
                                                    self.rf, self.volat, "EUR", cst.ASIAN, 30)

    def test_pricing_BSM(self):

        # Vanilla

        callValue = self.myVanillaCallPricer.pricingBSM()

        print("Valeur du call, pricé avec Black & Scholes : ")
        print(callValue)
        print('\n\n')

        putValue = self.myVanillaPutPricer.pricingBSM()

        print("Valeur du put, pricé avec Black & Scholes : ")
        print(putValue)
        print('\n\n')

        # Asian

        asianCallValue = self.myAsianCallPricer.pricingBSM()

        print("Valeur du call asian, pricé avec Black & Scholes : ")
        print(asianCallValue)
        print('\n\n')

        asianPutValue = self.myAsianPutPricer.pricingBSM()

        print("Valeur du put asian, pricé avec Black & Scholes : ")
        print(asianPutValue)
        print('\n\n')

        # Barrier

        barrierCallValue = self.myBarrierCallPricer.pricingBSM()

        print("Valeur du call barrière 80, pricé avec Black & Scholes : ")
        print(barrierCallValue)
        print('\n\n')

        barrierPutValue = self.myBarrierPutPricer.pricingBSM()

        print("Valeur du put barrière 80, pricé avec Black & Scholes : ")
        print(barrierPutValue)
        print('\n\n')

        test_call_vanilla = callValue > self.spot - self.strike and callValue < self.spot
        test_put_vanilla = putValue > self.strike - self.spot and putValue < self.spot

        test_call_asian = asianCallValue > self.spot - self.strike and asianCallValue < self.spot
        test_put_asian = asianPutValue > self.strike - self.spot and asianPutValue < self.spot

        test_call_barrier = barrierCallValue > self.spot - self.strike and barrierCallValue < self.spot
        test_put_barrier = barrierPutValue > self.strike - self.spot and barrierPutValue < self.spot

        self.assertTrue(test_call_vanilla)
        self.assertTrue(test_put_vanilla)
        self.assertTrue(test_call_asian)
        self.assertTrue(test_put_asian)
        self.assertTrue(test_call_barrier)
        self.assertTrue(test_put_barrier)

    def test_pricing_binom(self):

        # Vanilla

        callValue = self.myVanillaCallPricer.pricingBinomial(1000)

        print("Valeur du call, pricé avec un Arbre Binomial : ")
        print(callValue)
        print('\n\n')

        putValue = self.myVanillaPutPricer.pricingBinomial(1000)

        print("Valeur du put, pricé avec un Arbre Binomial : ")
        print(putValue)
        print('\n\n')

        # Asian

        asianCallValue = self.myAsianCallPricer.pricingBinomial(1000)

        print("Valeur du call asian, pricé avec un Arbre Binomial : ")
        print(asianCallValue)
        print('\n\n')

        asianPutValue = self.myAsianPutPricer.pricingBinomial(1000)

        print("Valeur du put asian, pricé avec un Arbre Binomial : ")
        print(asianPutValue)
        print('\n\n')

        # Barrier

        barrierCallValue = self.myBarrierCallPricer.pricingBinomial(1000)

        print("Valeur du call barrière 80, pricé avec un Arbre Binomial : ")
        print(barrierCallValue)
        print('\n\n')

        barrierPutValue = self.myBarrierPutPricer.pricingBinomial(1000)

        print("Valeur du put barrière 80, pricé avec un Arbre Binomial : ")
        print(barrierPutValue)
        print('\n\n')

        test_call_vanilla = callValue > self.spot - self.strike and callValue < self.spot
        test_put_vanilla = putValue > self.strike - self.spot and putValue < self.spot

        test_call_asian = asianCallValue > self.spot - self.strike and asianCallValue < self.spot
        test_put_asian = asianPutValue > self.strike - self.spot and asianPutValue < self.spot

        test_call_barrier = barrierCallValue > self.spot - self.strike and barrierCallValue < self.spot
        test_put_barrier = barrierPutValue > self.strike - self.spot and barrierPutValue < self.spot

        self.assertTrue(test_call_vanilla)
        self.assertTrue(test_put_vanilla)
        self.assertTrue(test_call_asian)
        self.assertTrue(test_put_asian)
        self.assertTrue(test_call_barrier)
        self.assertTrue(test_put_barrier)

    def test_pricing_MC(self):

        # Vanilla

        callValue = self.myVanillaCallPricer.pricingMonteCarlo(100)

        print("Valeur du call, pricé avec Monte Carlo : ")
        print(callValue)
        print('\n\n')

        putValue = self.myVanillaPutPricer.pricingMonteCarlo(100)

        print("Valeur du put, pricé avec Monte Carlo : ")
        print(putValue)
        print('\n\n')

        # Asian

        asianCallValue = self.myAsianCallPricer.pricingMonteCarlo(100)

        print("Valeur du call asian, pricé avec un Monte Carlo : ")
        print(asianCallValue)
        print('\n\n')

        asianPutValue = self.myAsianPutPricer.pricingMonteCarlo(100)

        print("Valeur du put asian, pricé avec un Monte Carlo : ")
        print(asianPutValue)
        print('\n\n')

        # Barrier

        barrierCallValue = self.myBarrierCallPricer.pricingMonteCarlo(100)

        print("Valeur du call barrière 80, pricé avec un Monte Carlo : ")
        print(barrierCallValue)
        print('\n\n')

        barrierPutValue = self.myBarrierPutPricer.pricingMonteCarlo(100)

        print("Valeur du put barrière 80, pricé avec un Monte Carlo : ")
        print(barrierPutValue)
        print('\n\n')

        test_call_vanilla = callValue > self.spot - self.strike and callValue < self.spot
        test_put_vanilla = putValue > self.strike - self.spot and putValue < self.spot

        test_call_asian = asianCallValue > self.spot - self.strike and asianCallValue < self.spot
        test_put_asian = asianPutValue > self.strike - self.spot and asianPutValue < self.spot

        test_call_barrier = barrierCallValue > self.spot - self.strike and barrierCallValue < self.spot
        test_put_barrier = barrierPutValue > self.strike - self.spot and barrierPutValue < self.spot

        self.assertTrue(test_call_vanilla)
        self.assertTrue(test_put_vanilla)
        self.assertTrue(test_call_asian)
        self.assertTrue(test_put_asian)
        self.assertTrue(test_call_barrier)
        self.assertTrue(test_put_barrier)


class TestPricerIface(unittest.TestCase):

    def test_pricer_iface(self):

        suceed = True

        try:
            myIface = ParamInterface()

            print("Veuillez effectuer une pricing sur le GUI de l'application ... ")

            myIface.mainloop()

            if myIface.var_product.get() == 'call':
                product_type = 'call'
            elif myIface.var_product.get() == 'put':
                product_type = 'put'
            else:
                product_type = 'call'

            if myIface.check_Convert.get() == 1:
                devisePricing = myIface.convert_devise.get()
            else:
                devisePricing = "EUR"

            if myIface.pricingMethod.curselection() == cst.BLACKSCHOLES:
                methodPricing = myIface.pricingMethod.get(cst.BLACKSCHOLES[0])
            elif myIface.pricingMethod.curselection() == cst.MONTECARLO:
                methodPricing = myIface.pricingMethod.get(cst.MONTECARLO[0])
            elif myIface.pricingMethod.curselection() == cst.BINOMIAL:
                methodPricing = myIface.pricingMethod.get(cst.BINOMIAL[0])
            else:
                methodPricing = cst.BSM_NAME

            try:
                strike = myIface.strike.get()
            except:
                strike = 100

            try:
                spot = myIface.spot.get()
            except:
                spot = 100

            try:
                taux_sans_risque = myIface.taux_sans_risque.get()
            except:
                taux_sans_risque = 0.02

            try:
                maturite = myIface.maturite.get()
            except:
                maturite = 1

            try:
                volat = myIface.volat.get()
            except:
                volat = 0.05

            print("Nous allons pricer un ", product_type, ", en ", devisePricing, " par la méthode, ", methodPricing, ".")
            print("Caractéristique de l'option : ")
            print("Strike : ", strike)
            print("Spot : ", spot)
            print("Taux sans risque : ", taux_sans_risque)
            print("Volatilité : ", volat)
            print("Maturité : ", maturite)

            myIface.destroy()

        except:
            suceed = False

        self.assertTrue(suceed)
