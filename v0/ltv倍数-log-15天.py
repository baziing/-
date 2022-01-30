import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import math
import sympy as sy
import matplotlib.pyplot as plt

def fun(x,a,b,c):
    return a*sy.log(b*x+c)

def funltv(x,a,b,c,base):
    return base*fun(x,a,b,c)

def funexp(x,n,a,b,c):
    mul=(x*b+c)**(n*a)
    return mul

if __name__ == '__main__':
    data = pd.read_csv('../data/test.csv')
    data['amount']=data['amount']/1000000
    data['ppl']=data['ppl']/1000000
    print(data)

    a, b, c = sy.symbols("a b c")
    eqList = []

    mul=1
    for i in range(0,5):
        mul=mul*funexp(5-i,data.loc[i,'ppl'],1,b,c)
    mul=mul-2.7**data['amount'][0:5].sum()
    eqList.append(sy.simplify(mul))

    mul=1
    for i in range(0,10):
        mul = mul * funexp(10-i, data.loc[i, 'ppl'], 1, b, c)
    mul = mul - 2.7**data['amount'][0:10].sum()
    eqList.append(sy.simplify(mul))

    for i in range(0,15):
        mul = mul * funexp(15-i, data.loc[i, 'ppl'], 1, b, c)
    mul = mul - 2.7**data['amount'][0:15].sum()
    eqList.append(sy.simplify(mul))

    print(len(eqList))
    print(eqList)
    result = sy.nonlinsolve(eqList, [ b,c])
    print(result)