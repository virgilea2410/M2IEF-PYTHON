#!python3

from PricerIface import *
import Pricer
import Option
import Stock
import os
import sys


class ApplicationPricer:

    def __init__(self):
        pass

    @staticmethod
    def run_pricing():

        endPricing = False

        while not endPricing:
            myIface = ParamInterface()
            myIface.mainloop()

            # Getting the product type input

            if myIface.var_product.get().upper() == cst.CALL:
                product_type = cst.CALL
            elif myIface.var_product.get().upper() == cst.PUT:
                product_type = cst.PUT
            else:
                product_type = cst.CALL

            # Getting the option features
            if myIface.var_feature.get().upper() == cst.VANILLA:
                feature = cst.VANILLA
                feature_val = 0.00
            elif myIface.var_feature.get().upper() == cst.BARRIER:
                feature = cst.BARRIER
                try:
                    feature_val = myIface.feature.get()
                except:
                    feature_val = 70
            elif myIface.var_feature.get().upper() == cst.ASIAN:
                feature = cst.ASIAN
                try:
                    feature_val = myIface.feature.get()
                except:
                    feature_val = 30
            else:
                feature = cst.VANILLA
                feature_val = 0.00

            # Getting the currency input and the corresponding change rate

            if myIface.check_Convert.get() == 1:
                devisePricing = str(myIface.convert_devise.get())
            else:
                devisePricing = cst.AVAIL_CCY[cst.EUR]

            if devisePricing in cst.AVAIL_CCY:
                if devisePricing == cst.AVAIL_CCY[cst.EUR]:
                    change_rate = cst.EUREUR
                elif devisePricing == cst.AVAIL_CCY[cst.USD]:
                    change_rate = cst.EURUSD
                elif devisePricing == cst.AVAIL_CCY[cst.GBP]:
                    change_rate = cst.EURGBP
                elif devisePricing == cst.AVAIL_CCY[cst.AUD]:
                    change_rate = cst.EURAUD
                elif devisePricing == cst.AVAIL_CCY[cst.JPY]:
                    change_rate = cst.EURJPY
                elif devisePricing == cst.AVAIL_CCY[cst.CHF]:
                    change_rate = cst.EURCHF
                elif devisePricing == cst.AVAIL_CCY[cst.CAD]:
                    change_rate = cst.EURCAD
                elif devisePricing == cst.AVAIL_CCY[cst.BTC]:
                    change_rate = cst.EURBTC
                elif devisePricing == cst.AVAIL_CCY[cst.NZD]:
                    change_rate = cst.EURNZD
                elif devisePricing == cst.AVAIL_CCY[cst.CNY]:
                    change_rate = cst.EURCNY
                elif devisePricing == cst.AVAIL_CCY[cst.BRL]:
                    change_rate = cst.EURBRL
                elif devisePricing == cst.AVAIL_CCY[cst.SEK]:
                    change_rate = cst.EURSEK
                else:
                    change_rate = cst.EUREUR
            else:
                devisePricing = cst.AVAIL_CCY[cst.EUR]
                change_rate = cst.EUREUR

            # Getting the pricing method input

            if myIface.pricingMethod.curselection() == cst.BLACKSCHOLES:
                methodPricing = myIface.pricingMethod.get(cst.BLACKSCHOLES[0])
            elif myIface.pricingMethod.curselection() == cst.MONTECARLO:
                methodPricing = myIface.pricingMethod.get(cst.MONTECARLO[0])
            elif myIface.pricingMethod.curselection() == cst.BINOMIAL:
                methodPricing = myIface.pricingMethod.get(cst.BINOMIAL[0])
            else:
                methodPricing = myIface.pricingMethod.get(cst.BLACKSCHOLES[0])

            # Getting the spot input

            try:
                spot = float(myIface.spot.get())
            except:
                spot = 100.00

            # getting the strike input

            if myIface.strike.get() != 0.00:
                strike = float(myIface.strike.get()/100.00 * spot)
            else:
                strike = 100.00

            # Getting the risk free rate input

            try:
                taux_sans_risque = float(myIface.taux_sans_risque.get())
            except:
                taux_sans_risque = 0.02

            # Getting the tenor input

            try:
                maturite = float(myIface.maturite.get())
            except:
                maturite = 1

           # Getting the volatility input

            try:
                volat = float(myIface.volat.get())
            except:
                volat = 0.05

            # Setting the pricing currency

            try:
                devise = devisePricing
            except:
                devise = cst.AVAIL_CCY[cst.EUR]

            # Getting the number of simulation input (for MC and Binomial methods only)

            try:
                nbSimul = int(myIface.nbSimul.get())
            except:
                pass

            # Destroy

            myIface.cadre1.destroy()
            myIface.Tk.destroy()
            # myIface.destroy()

            # Initialisation de l'Option et du Stock

            myStock = Stock.Stock('APPLE', spot, volat)
            myOption = Option.Option(myStock, product_type, strike, myStock.price, myStock.sigma, maturite, taux_sans_risque, 100.00, feature, feature_val)

            # Initialisation des Pricers

            # myPricer = Pricer.OptionPricer(product_type, strike, spot, maturite, taux_sans_risque, volat, devisePricing)
            myPricer = Pricer.OptionPricer(myOption=myOption, devise=devise)

            val = 0.00

            # setting the pricing method and computing the option price with it
            try:
                if methodPricing == cst.BSM_NAME:
                    val = myPricer.pricingBSM() * change_rate
                elif methodPricing == cst.BINOM_NAME:
                    val = myPricer.pricingBinomial(nbSimul) * change_rate
                elif methodPricing == cst.MC_NAME:
                   val = myPricer.pricingMonteCarlo(nbSimul) * change_rate
                else:
                    val = myPricer.pricingBSM() * change_rate
            except:
                val = "Pricing Failed"

            # Initialisation puis affichage de l'Interface des résultats du pricing

            myResultIface = ResultInterface(myPricer, methodPricing, val)
            myResultIface.mainloop()

            endPricing = myResultIface.end

            # Destroy
            myResultIface.destroy()

    @staticmethod
    def test_pricing():

        dir = os.getcwd()
        python_path = sys.executable

        if os.name == 'posix' or os.name == 'mac':

            os.system("cd " + dir + "; " + python_path + " -m unittest UnitaryTest")

        elif os.name == "nt" or os.name == "win32":

            os.system("cd + " + dir + " && " + python_path + " -m unittest UnitaryTest")

