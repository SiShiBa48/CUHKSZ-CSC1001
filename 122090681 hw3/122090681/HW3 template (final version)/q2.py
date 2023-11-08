#### Please do not use input() function!!!
class process_derivative(object):

    def __init__(self, polynominal):
        self.polynominal = polynominal
    def strr(self,m,p,wor):
        a = m * p
        b = p - 1
        if b == 0:
            re = str(a)
            return re
        if b == 1:
            re = str(a) + "*" + wor
            return re
        aa = str(a)
        bb = str(b)
        re = aa + "*" + wor + "^" + bb
        return re
    def get_first_derivative(self):
        # You should follow the example format. Do not use input()
        mu = False
        mu1 = 0
        pow = False
        pow1 = 0
        ans = ""
        word = ""
        de = True
        for i in self.polynominal:
            if (i=="+")or(i=="-"):
                de = False
                if mu and pow:
                    if mu1 * pow1 != 0:
                        ans = ans + self.strr(mu1,pow1,word) + i
                    mu = False
                    pow = False
                    mu1 = 0
                    pow1 = 0
                if mu and (not pow):
                    g = str(mu1)
                    ans = ans + g + i
                    mu = False
                    pow = False
                    mu1 = 0
                    pow1 = 0
                if not mu:
                    mu = False
                    pow = False
                    mu1 = 0
                    pow1 = 0
            if i.isdigit():
                j = int(i)
                if mu == False:
                    mu1 = mu1*10 + j
                if mu and pow:
                    pow1 = pow1*10 + j
            if i == "*":
                mu = True
            if i == "^":
                pow = True
            if i.isalpha():
                word = i
        if de:
            if mu and pow:
                    ans = ans + self.strr(mu1,pow1,word)
                    mu = False
                    pow = False
                    mu1 = 0
                    pow1 = 0
            elif mu and (not pow):
                g = str(mu1)
                ans = ans + g
                mu = False
                pow = False
                mu1 = 0
                pow1 = 0
            elif not mu:
                mu = False
                pow = False
                mu1 = 0
                pow1 = 0
                ans = "0"
            return "The first derivative is:" + ans
        if mu and pow:
            if mu1 * pow1 != 0:
                ans = ans + self.strr(mu1,pow1,word)
            mu = False
            pow = False
            mu1 = 0
            pow1 = 0
        if mu and (not pow):
            g = str(mu1)
            ans = ans + g
            mu = False
            pow = False
            mu1 = 0
            pow1 = 0
        if not mu:
            mu = False
            pow = False
            mu1 = 0
            pow1 = 0
        if (ans[-1]=="+")or(ans[-1]=="-"):
            ans = ans[:-1]
        if self.polynominal[0] == "-":
            if self.polynominal[1] != "0":
                ans = "-" + ans
        return "The first derivative is:" + ans
#@test = process_derivative("4*x+33+3*x^56")  
#result = test.get_first_derivative()
#print(result)     