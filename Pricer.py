#!python3

import scipy.stats as stats
import random
import numpy
import PricerConstants as cst


class OptionPricer:

    def __init__(self, optionType=cst.CALL, strike=100.00, spot=100.00, maturite=1, taux_sans_risque=0.02, volat=0.05, devise="EUR", feature='NONE', feature_val=0.00, myOption=None):

        if myOption is None:
            self.optionType = str(optionType)
            self.strike = float(strike)
            self.spot = float(spot)
            self.maturite = float(maturite)
            self.taux_sans_risque = float(taux_sans_risque)
            self.volat = float(volat)
            self.devise = str(devise)
            self.feature = str(feature.upper())
            self.featureval = float(feature_val)
            self.delta = float()
            self.vega = float()
            self.gamma = float()

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

        else:
            self.optionType = str(myOption.type)
            self.strike = float(myOption.strike)
            self.spot = float(myOption.spot)
            self.maturite = float(myOption.maturite)
            self.taux_sans_risque = float(myOption.risk_free_rate)
            self.volat = float(myOption.volat)
            self.devise = str(devise)
            self.feature = str(myOption.feature.upper())
            self.delta = float()
            self.vega = float()
            self.gamma = float()

            if self.feature == cst.VANILLA or self.feature == "NONE":
                pass

            elif self.feature == cst.BARRIER:
                if myOption.barrier == 0.00:
                    self.barrier = 0.7 * self.strike
                else:
                    self.barrier = float(myOption.barrier) / 100 * self.strike

            elif self.feature == cst.ASIAN:
                if myOption.asian_days == 0.00:
                    self.asian_days = 30
                else:
                    self.asian_days = myOption.asian_days

    def pricingBSM(self):

        d1 = float(1/(self.volat * numpy.sqrt(self.maturite)) * (numpy.log(self.spot/self.strike) + (self.taux_sans_risque + 1/2 * pow(self.volat, 2)) * self.maturite))
        d2 = float(d1 - self.volat * numpy.sqrt(self.maturite))

        value = 0.00

        try:

            if self.optionType.upper() == cst.CALL:

                if self.feature.upper() == cst.VANILLA or self.feature.upper() == cst.NONE:

                    value = float(self.spot * stats.norm.cdf(d1) - self.strike * numpy.exp(-self.taux_sans_risque * self.maturite) * stats.norm.cdf(d2))
                    self.delta = stats.norm.cdf(d1)
                    self.vega = float(self.spot * numpy.sqrt(self.maturite) * stats.norm.pdf(d1))
                    self.gamma = float(stats.norm.pdf(d1) / (self.spot * self.volat * numpy.sqrt(self.maturite)))

                elif self.feature.upper() == cst.ASIAN:

                    j = 0
                    # n = self.asian_days
                    n = 1
                    S0 = self.spot
                    sig = self.volat/365
                    mat = self.maturite * 365
                    k = self.strike
                    rf = self.taux_sans_risque/365
                    h = 1/365

                    B0 = 1
                    Bverif = 1
                    i = 1
                    while i <= n:
                        Bverif = Bverif * (((mat-(n-j))*h))
                        i += 1

                    Bverif = pow(Bverif, (1/n))

                    T2 = pow(((n-j)/n), 2) * mat - (((n-j)*(n-j-1)*(4*n - 4*j + 1))/pow(6*n, 2)) * h
                    T1 = ((n-j)/n) * (mat - ((n - j - 1) * h)/2)
                    A0 = numpy.exp(-rf*(mat-T1) - pow(sig, 2)*(T1 - T2)/2) * B0
                    d0 = (numpy.log(S0/k) + (rf - pow(sig, 2)/2)*T1 + numpy.log(B0))/(sig * numpy.sqrt(T2))

                    d1 = d0 + sig * numpy.sqrt(T2)

                    value = S0 * A0 * stats.norm.cdf(d1) - k * numpy.exp(-rf * mat) * stats.norm.cdf(d0)

                    self.delta = A0 * stats.norm.cdf(d1)
                    self.vega = float(self.spot * numpy.sqrt(self.maturite) * stats.norm.pdf(d1))
                    self.gamma = float(stats.norm.pdf(d1) / (self.spot * self.volat * numpy.sqrt(self.maturite)))

                elif self.feature.upper() == cst.BARRIER:

                    phi = 1
                    theta = 1

                    S0 = self.spot
                    sig = self.volat
                    mat = self.maturite
                    K = self.strike
                    rf = self.taux_sans_risque
                    mu = self.taux_sans_risque

                    H = self.barrier

                    a = mu/(pow(sig, 2))
                    b = numpy.sqrt(pow(mu, 2) + 2 * pow(sig, 2) * rf)

                    lamb = 1 + (mu / pow(sig, 2))
                    z =  numpy.log(H/S0)/(sig*numpy.sqrt(mat)) + b * sig * numpy.sqrt(mat)

                    x = numpy.log(S0/K)/(sig*numpy.sqrt(mat)) + lamb * sig * numpy.sqrt(mat)
                    x1 = numpy.log(S0/H)/(sig*numpy.sqrt(mat)) + lamb * sig * numpy.sqrt(mat)

                    y = numpy.log(pow(H, 2)/S0*K)/sig*numpy.sqrt(mat) + lamb * sig * numpy.sqrt(mat)
                    y1 = numpy.log(H/S0)/(sig*numpy.sqrt(mat)) + lamb * sig * numpy.sqrt(mat)

                    I1 = phi * S0 * numpy.exp(-1 / 365) * stats.norm.cdf(phi * x) - phi * K * \
                         numpy.exp(-rf * mat) * stats.norm.cdf(phi * x - phi * sig * numpy.sqrt(mat))

                    I2 = phi * S0 * numpy.exp(-1 / 365) * stats.norm.cdf(phi * x1) - phi * K * \
                         numpy.exp(-rf * mat) * stats.norm.cdf(phi * x1 - phi * sig * numpy.sqrt(mat))

                    I3 = phi * S0 * numpy.exp(-1/365) * pow((H/S0), 2 * lamb) * stats.norm.cdf(theta * y) - \
                         phi * K * numpy.exp(-rf * mat) * pow((H/S0), 2*lamb - 2) * \
                         stats.norm.cdf(theta*y - theta * sig * numpy.sqrt(mat))

                    I4 = phi * S0 * numpy.exp(-1 / 365) * pow((H / S0), 2 * lamb) * stats.norm.cdf(theta * y1) - \
                         phi * K * numpy.exp(-rf * mat) * pow((H / S0), 2 * lamb - 2) * \
                         stats.norm.cdf(theta * y1 - theta * sig * numpy.sqrt(mat))

                    I5 = numpy.pi * numpy.exp(-rf * mat) * (stats.norm.cdf(theta * x1 - theta * sig * numpy.sqrt(mat)) - pow((H/S0), 2*lamb - 2) * stats.norm.cdf(theta * y1 - theta * sig * numpy.sqrt(mat)))

                    if K > H:
                        value = I3 + I5
                    elif K < H:
                        value = I1 - I2 + I4 + I5
                    else:
                        value = I3 + I5 + I1 - I2 + I4 + I5

                    self.delta = stats.norm.cdf(x)
                    self.vega = float(self.spot * numpy.sqrt(self.maturite) * stats.norm.pdf(x))
                    self.gamma = float(stats.norm.pdf(x) / (self.spot * self.volat * numpy.sqrt(self.maturite)))

            elif self.optionType.upper() == cst.PUT:

                if self.feature.upper() == cst.VANILLA or self.feature.upper() == cst.NONE:

                    value = float(-self.spot * stats.norm.cdf(-d1) + self.strike * numpy.exp(-self.taux_sans_risque * self.maturite) * stats.norm.cdf(-d2))
                    self.delta = stats.norm.cdf(d1) - 1
                    self.vega = float(self.spot * numpy.sqrt(self.maturite) * stats.norm.pdf(d1))
                    self.gamma = float(stats.norm.pdf(d1) / (self.spot * self.volat * numpy.sqrt(self.maturite)))

                elif self.feature.upper() == cst.ASIAN:

                    j = 0
                    n = 30
                    S0 = self.spot
                    sig = self.volat/365
                    mat = self.maturite * 365
                    k = self.strike
                    rf = self.taux_sans_risque/365
                    h = 1

                    B0 = 1
                    # verif =
                    T2 = pow(((n-j)/n), 2) * mat - (((n-j)*(n-j-1)*(4*n - 4*j + 1))/pow(6*n, 2)) * h
                    T1 = ((n-j)/n) * (mat - ((n - j - 1) * h)/2)
                    A0 = numpy.exp(-rf*(mat-T1) - pow(sig, 2)*(T1 - T2)/2) * B0
                    d0 = (numpy.log(S0/k) + (rf - pow(sig, 2)/2)*T1 + numpy.log(B0))/(sig * numpy.sqrt(T2))

                    d1 = d0 + sig * numpy.sqrt(T2)

                    value = k * numpy.exp(-rf * mat) * stats.norm.cdf(-d0) - S0 * A0 * stats.norm.cdf(-d1)

                    self.delta = A0 * stats.norm.cdf(d1) - 1
                    self.vega = float(self.spot * numpy.sqrt(self.maturite) * stats.norm.pdf(d1))
                    self.gamma = float(stats.norm.pdf(d1) / (self.spot * self.volat * numpy.sqrt(self.maturite)))

                elif self.feature.upper() == cst.BARRIER:

                    phi = -1
                    theta = 1

                    S0 = self.spot
                    sig = self.volat
                    mat = self.maturite
                    K = self.strike
                    rf = self.taux_sans_risque
                    mu = self.taux_sans_risque

                    H = self.barrier

                    a = mu/(pow(sig, 2))
                    b = numpy.sqrt(pow(mu, 2) + 2 * pow(sig, 2) * rf)

                    lamb = 1 + (mu / pow(sig, 2))
                    z =  numpy.log(H/S0)/(sig*numpy.sqrt(mat)) + b * sig * numpy.sqrt(mat)

                    x = numpy.log(S0/K)/(sig*numpy.sqrt(mat)) + lamb * sig * numpy.sqrt(mat)
                    x1 = numpy.log(S0/H)/(sig*numpy.sqrt(mat)) + lamb * sig * numpy.sqrt(mat)

                    y = numpy.log(pow(H, 2)/S0*K)/sig*numpy.sqrt(mat) + lamb * sig * numpy.sqrt(mat)
                    y1 = numpy.log(H/S0)/(sig*numpy.sqrt(mat)) + lamb * sig * numpy.sqrt(mat)

                    I1 = phi * S0 * numpy.exp(-1 / 365) * stats.norm.cdf(phi * x) - phi * K * \
                         numpy.exp(-rf * mat) * stats.norm.cdf(phi * x - phi * sig * numpy.sqrt(mat))

                    I2 = phi * S0 * numpy.exp(-1 / 365) * stats.norm.cdf(phi * x1) - phi * K * \
                         numpy.exp(-rf * mat) * stats.norm.cdf(phi * x1 - phi * sig * numpy.sqrt(mat))

                    I3 = phi * S0 * numpy.exp(-1/365) * pow((H/S0), 2 * lamb) * stats.norm.cdf(theta * y) - \
                         phi * K * numpy.exp(-rf * mat) * pow((H/S0), 2*lamb - 2) * \
                         stats.norm.cdf(theta*y - theta * sig * numpy.sqrt(mat))

                    I4 = phi * S0 * numpy.exp(-1 / 365) * pow((H / S0), 2 * lamb) * stats.norm.cdf(theta * y1) - \
                         phi * K * numpy.exp(-rf * mat) * pow((H / S0), 2 * lamb - 2) * \
                         stats.norm.cdf(theta * y1 - theta * sig * numpy.sqrt(mat))

                    I5 = numpy.pi * numpy.exp(-rf * mat) * (stats.norm.cdf(theta * x1 - theta * sig * numpy.sqrt(mat)) - pow((H/S0), 2*lamb - 2) * stats.norm.cdf(theta * y1 - theta * sig * numpy.sqrt(mat)))

                    if K > H:
                        value = I2 - I3 + I4 + I5
                    elif K < H:
                        value = I1 + I5
                    else:
                        value = I2 - I3 + I4 + I5 + I1 + I5

                    self.delta = stats.norm.cdf(x) - 1
                    self.vega = float(self.spot * numpy.sqrt(self.maturite) * stats.norm.pdf(x))
                    self.gamma = float(stats.norm.pdf(x) / (self.spot * self.volat * numpy.sqrt(self.maturite)))

            else:

                value = 0
                self.delta = 0
                self.vega = 0
                self.gamma = 0
                print("Runtime Error : No option type specified")

        except(RuntimeError, ValueError, NameError, TypeError):

            value = 0
            self.delta = 0
            self.vega = 0
            self.gamma = 0
            print("Runtime Error : Pricing failed")

        return value

    def pricingBinomial(self, num_iteration):

        u = float(numpy.exp(self.volat * numpy.sqrt(1/num_iteration)))
        d = 1/u
        q = float((numpy.exp(self.taux_sans_risque * 1 / num_iteration) - d) / (u - d))

        # Main path in order to compute the Price

        path = list()
        marktVal = list()

        # epsilons for variable variations

        h = 0.0001
        eps = 0.0001
        w = 0.0001

        # Secondary path in order to compute the Delta

        path2 = list()
        marktVal2 = list()

        # Third path with modified risk-neutral probability ans u & d probs, in order to compute vega

        path3 = list()
        marktVal3 = list()

        u_3 = float(numpy.exp((self.volat + eps) * numpy.sqrt(1/num_iteration)))
        d_3 = 1/u_3
        q_3 = float((numpy.exp(self.taux_sans_risque * 1/num_iteration)-d_3)/(u_3-d_3))

        # Fourth path in order to compute the Gamma

        path4 = list()
        marktVal4 = list()

        # Construction de l'arbre

        ubound = int(round(num_iteration * self.maturite, 0))

        i = 0
        while i < ubound:
            if i == 0:
                path.append(list())
                path[i].append(self.spot)

                path2.append(list())
                path2[i].append(self.spot + h)

                path3.append(list())
                path3[i].append(self.spot)

                path4.append(list())
                path4[i].append(self.spot + w + h)
                # path4[i].append(self.spot - h)

                marktVal.append(list())
                marktVal2.append(list())
                marktVal3.append(list())
                marktVal4.append(list())

            # else:
            path.append(list())
            marktVal.append(list())

            path2.append(list())
            marktVal2.append(list())

            path3.append(list())
            marktVal3.append(list())

            path4.append(list())
            marktVal4.append(list())

            j = 0
            while j <= i:

                path[i+1].append(d * path[i][j])

                path2[i + 1].append(d * path2[i][j])

                path3[i + 1].append(d_3 * path3[i][j])

                path4[i + 1].append(d * path4[i][j])

                if j == i:

                    path[i+1].append(u * path[i][j])

                    path2[i + 1].append(u * path2[i][j])

                    path3[i + 1].append(u_3 * path3[i][j])

                    path4[i + 1].append(u * path4[i][j])

                j += 1

            i += 1

        # Pricing de l'option

        j = ubound - 1

        while j >= 0:
            i = 0
            while i <= j:
                if j == ubound - 1:

                    if self.optionType.upper() == cst.CALL:
                        if self.feature.upper() == cst.VANILLA or self.feature.upper() == cst.NONE:
                            marktVal[j].append((1-q) * (path[j + 1][i] - self.strike) + q * (path[j + 1][i + 1] - self.strike))
                            marktVal2[j].append((1 - q) * (path2[j + 1][i] - self.strike) + q * (path2[j + 1][i + 1] - self.strike))
                            marktVal3[j].append((1 - q_3) * (path3[j + 1][i] - self.strike) + q_3 * (path3[j + 1][i + 1] - self.strike))
                            marktVal4[j].append((1 - q) * (path4[j + 1][i] - self.strike) + q * (path4[j + 1][i + 1] - self.strike))

                        elif self.feature.upper() == cst.ASIAN:
                            marktVal[j].append((1-q) * (path[j + 1][i] - self.strike) + q * (path[j + 1][i + 1] - self.strike))
                            marktVal2[j].append((1 - q) * (path2[j + 1][i] - self.strike) + q * (path2[j + 1][i + 1] - self.strike))
                            marktVal3[j].append((1 - q_3) * (path3[j + 1][i] - self.strike) + q_3 * (path3[j + 1][i + 1] - self.strike))
                            marktVal4[j].append((1 - q) * (path4[j + 1][i] - self.strike) + q * (path4[j + 1][i + 1] - self.strike))

                        elif self.feature.upper() == cst.BARRIER:
                            marktVal[j].append((1-q) * (path[j + 1][i] - self.strike) + q * (path[j + 1][i + 1] - self.strike))
                            marktVal2[j].append((1 - q) * (path2[j + 1][i] - self.strike) + q * (path2[j + 1][i + 1] - self.strike))
                            marktVal3[j].append((1 - q_3) * (path3[j + 1][i] - self.strike) + q_3 * (path3[j + 1][i + 1] - self.strike))
                            marktVal4[j].append((1 - q) * (path4[j + 1][i] - self.strike) + q * (path4[j + 1][i + 1] - self.strike))

                    if self.optionType.upper() == cst.PUT:
                        if self.feature.upper() == cst.VANILLA or self.feature.upper() == cst.NONE:
                            marktVal[j].append((1-q) * (self.strike - path[j + 1][i]) + q * (self.strike - path[j + 1][i + 1]))
                            marktVal2[j].append((1 - q) * (self.strike - path2[j + 1][i]) + q * (self.strike - path2[j + 1][i + 1]))
                            marktVal3[j].append((1 - q_3) * (self.strike - path3[j + 1][i]) + q_3 * (self.strike - path3[j + 1][i + 1]))
                            marktVal4[j].append((1 - q) * (self.strike - path4[j + 1][i]) + q * (self.strike - path4[j + 1][i + 1]))

                        elif self.feature.upper() == cst.ASIAN:
                            marktVal[j].append((1-q) * (self.strike - path[j + 1][i]) + q * (self.strike - path[j + 1][i + 1]))
                            marktVal2[j].append((1 - q) * (self.strike - path2[j + 1][i]) + q * (self.strike - path2[j + 1][i + 1]))
                            marktVal3[j].append((1 - q_3) * (self.strike - path3[j + 1][i]) + q_3 * (self.strike - path3[j + 1][i + 1]))
                            marktVal4[j].append((1 - q) * (self.strike - path4[j + 1][i]) + q * (self.strike - path4[j + 1][i + 1]))

                        elif self.feature.upper() == cst.BARRIER:
                            marktVal[j].append((1-q) * (self.strike - path[j + 1][i]) + q * (self.strike - path[j + 1][i + 1]))
                            marktVal2[j].append((1 - q) * (self.strike - path2[j + 1][i]) + q * (self.strike - path2[j + 1][i + 1]))
                            marktVal3[j].append((1 - q_3) * (self.strike - path3[j + 1][i]) + q_3 * (self.strike - path3[j + 1][i + 1]))
                            marktVal4[j].append((1 - q) * (self.strike - path4[j + 1][i]) + q * (self.strike - path4[j + 1][i + 1]))

                else:

                    marktVal[j].append((1-q) * (marktVal[j + 1][i]) + q * (marktVal[j + 1][i + 1]))
                    marktVal2[j].append((1 - q) * (marktVal2[j + 1][i]) + q * (marktVal2[j + 1][i + 1]))
                    marktVal3[j].append((1 - q_3) * (marktVal3[j + 1][i]) + q_3 * (marktVal3[j + 1][i + 1]))
                    marktVal4[j].append((1 - q) * (marktVal4[j + 1][i]) + q * (marktVal4[j + 1][i + 1]))

                if marktVal[j][i] < 0:
                    marktVal[j][i] = 0
                if marktVal2[j][i] < 0:
                    marktVal2[j][i] = 0
                if marktVal3[j][i] < 0:
                    marktVal3[j][i] = 0
                if marktVal4[j][i] < 0:
                    marktVal4[j][i] = 0

                i += 1

            j -= 1

        price = marktVal[0][0] / pow((1+self.taux_sans_risque), self.maturite)
        price2 = marktVal2[0][0] / pow((1 + self.taux_sans_risque), self.maturite)
        price3 = marktVal3[0][0] / pow((1 + self.taux_sans_risque), self.maturite)
        price4 = marktVal4[0][0] / pow((1 + self.taux_sans_risque), self.maturite)

        self.delta = (price2 - price)/h

        # delta2 = (price4 - price2)/(w)

        # self.gamma = (self.delta - delta2)/pow((w+h), 2) # / self.delta
        self.gamma = (pow(price2, 2) - 2*price2*price + pow(price, 2)) / pow(h+w, 2)

        self.vega = (price3 - price)/eps

        return price

    def pricingMonteCarlo(self, num_iteration):

        # Initialisation

        result = list()
        num_iteration = int(num_iteration)
        delta = list()
        vega = list()
        gamma = list()
        mean_delta = list()
        mean_vega = list()
        mean_gamma = list()
        stock_price = list()
        option_price = list()
        ubound = int(round(self.maturite*365))
        hit_barrier = list()
        avg_strike = list()

        volat = self.volat * numpy.sqrt(1/365)
        rf = self.taux_sans_risque/365

        # Check feature

        if self.feature == cst.BARRIER:
            bool_hit = False
            self.asian_days = -1
        elif self.feature == cst.VANILLA or self.feature == cst.NONE:
            bool_hit = True
            self.barrier = 0
            self.asian_days = - 1
        elif self.feature == cst.ASIAN:
            bool_hit = True
            self.barrier = 0

            if self.asian_days == 0:
                self.asian_days = 30
            else:
                self.asian_days = float(self.asian_days)
        else:
            bool_hit = True
            self.barrier = 0

        # Main path

        i = 0
        while i < num_iteration:

            # 2-D Arrays initialisation

            result.append(list())
            result[i].append(self.spot)
            avg_strike.append(list())

            delta.append(list())
            vega.append(list())
            gamma.append(list())

            # One simulation path

            j = 1
            while j < ubound:

                val = float(result[i][j-1] * (1 + (self.taux_sans_risque * 1/365 + self.volat * numpy.sqrt(1/365) * stats.norm.ppf(random.uniform(0, 1)))))
                # val = result[i][j-1] * numpy.exp((rf - pow(volat, 2)/2) * self.maturite + volat * numpy.sqrt(self.maturite) * stats.norm.ppf(random.uniform(0, 1)))

                result[i].append(val)

                if val < self.barrier:
                    bool_hit = True

                if self.feature == cst.ASIAN and j <= self.asian_days:
                    avg_strike[i].append(val)
                    one_avg_strike = numpy.mean(avg_strike[i])
                    self.strike = one_avg_strike

                # Greeks calculations for each step

                if self.optionType.upper() == cst.CALL:

                    delta[i].append(
                        numpy.exp(-self.taux_sans_risque * self.maturite) * numpy.maximum(val - self.strike, 0) *
                        1 / (self.spot * pow(self.volat, 2) * self.maturite) *
                        (numpy.log(val / self.spot) + (self.taux_sans_risque - 0.5 * pow(self.volat, 2)) *
                        self.maturite)
                    )

                elif self.optionType.upper() == cst.PUT:

                    delta[i].append(
                        numpy.exp(-self.taux_sans_risque * self.maturite) * numpy.maximum(self.strike - val, 0) *
                        1 / (self.spot * pow(self.volat, 2) * self.maturite) *
                        (numpy.log(val / self.spot) + (self.taux_sans_risque - 0.5 * pow(self.volat, 2)) *
                        self.maturite)
                    )

                Z = (numpy.log(val / self.spot) - (
                        self.taux_sans_risque * 1 / 365 - pow(self.volat, 2) / 2) * self.maturite) / (
                            self.volat * numpy.sqrt(self.maturite))

                Pvega = (pow(Z, 2) - 1)/self.volat - Z * numpy.sqrt(self.maturite)
                vega[i].append(numpy.maximum(val - self.strike, 0) * Pvega)

                gamma[i].append(
                    -numpy.exp(-self.taux_sans_risque * self.maturite) * numpy.maximum(val - self.strike, 0) *
                    (pow(1/365, 2) - (1/365) * self.volat * numpy.sqrt(self.maturite) - 1) / (pow(self.spot, 2) * pow(self.volat, 2) * self.maturite)
                )

                if j == ubound - 1:

                    stock_price.append(val)

                    hit_barrier.append(bool_hit)

                    # if self.feature == cst.ASIAN:
                    #     one_avg_strike = numpy.mean(avg_strike[i])
                    #     self.strike = one_avg_strike

                    if self.optionType.upper() == cst.CALL:
                        option_price.append(numpy.maximum(stock_price[i] - self.strike, 0) *
                                            numpy.exp(-self.taux_sans_risque*self.maturite))

                    if self.optionType.upper() == cst.PUT:
                        option_price.append(numpy.maximum(self.strike - stock_price[i], 0) *
                                            numpy.exp(-self.taux_sans_risque*self.maturite))

                    mean_delta.append(numpy.mean(delta[i]))
                    mean_vega.append(numpy.mean(vega[i]))
                    mean_gamma.append(numpy.mean(gamma[i]))

                    if hit_barrier[i] == True:
                        option_price[i] = option_price[i]
                    elif hit_barrier[i] == False:
                        option_price[i] = 0

                j += 1

            i += 1

        price = numpy.mean(option_price)
        self.delta = numpy.mean(mean_delta)
        self.vega = numpy.mean(mean_vega)
        self.gamma = numpy.mean(mean_gamma)

        return price

    @staticmethod
    def getMethods():
        myList = list()

        myList.append(cst.BSM_NAME)
        myList.append(cst.BINOM_NAME)
        myList.append(cst.MC_NAME)

        return myList

    @staticmethod
    def help():
        print("Voici les méthodes de pricing disponible : ")

        for methods in OptionPricer.getMethods():
            print(methods)
        print('\n\n')
