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
    mul=a*sy.log(b*(x+70))
    mul=''
    mul=mul*n
    return mul

if __name__ == '__main__':
    data = pd.read_csv('../goc.csv')
    data['amount']=data['amount']/100/1000000
    data['ppl']=data['ppl']/1000000
    print(data)

    a, b, c = sy.symbols("a b c")
    eqList = []

    # mul=0
    # date=50
    # for i in range(0,int(date)):
    #     mul=mul+funexp(int(date)-i,data.loc[i,'ppl'],a,b,c)
    # mul=mul-data['amount'][0:int(date)].sum()
    # print(mul)
    # eqList.append(sy.simplify(mul))

    mul=0
    date=45
    for i in range(0,int(date)):
        mul = mul +funexp(int(date)-i, data.loc[i, 'ppl'], a, b,c)
        print(funexp(int(date)-i, data.loc[i, 'ppl'], a, b, c))
        # print(int(date)-i,data.loc[i, 'ppl'])
    mul = mul - data['amount'][0:int(date)].sum()
    eqList.append(sy.simplify(mul))

    mul=0
    date=90
    for i in range(0,int(date)):
        mul = mul +funexp(int(date)-i, data.loc[i, 'ppl'], a, b, c)
    mul = mul - data['amount'][0:int(date)].sum()
    eqList.append(sy.simplify(mul))

    print(len(eqList))
    print(eqList)
    result = sy.nonlinsolve(eqList, [a,b,c])
    print(result)