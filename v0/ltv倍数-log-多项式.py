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

def funexp(end,num,n,a,b,c,base):
    mul=1
    for i in range(end-num+1,end+1):
        mul=mul*(i*b+c)
    mul=mul**(n*base*a)
    # print(mul)
    return mul



if __name__ == '__main__':
    a,b,c=sy.symbols("a b c")

    data = pd.read_csv('../data/ltv.csv')
    data['n']=data['n']
    data['amount']=data['amount']
    data['日导量'] = data['n'] / data['day']
    eqList = []
    # eqList.append(fun(1,a,b,c)-1)
    for month in range(0,2):
        if month==0:
            print(data.loc[month,'day'])
            # eq=funexp(data.loc[month,'day'],data.loc[month,'day'],data.loc[month,'日导量'],1.8,b,c,1)-sy.exp(data.loc[month,'amount'])
            eq = funexp(data.loc[month, 'day'], data.loc[month, 'day'], data.loc[month, '日导量'], 1.8, b, c, 1) - 2.718**data.loc[month, 'amount']
            eqList.append(sy.simplify(eq))
            print(sy.simplify(eq))
        else:
            eq=0
            for i in range(0,month):
                maxday=data['day'][i:month+1].sum()
                eq=eq+funexp(maxday,data.loc[i,'day'],data.loc[i,'日导量'],1.8,b,c,1)
            # eq=eq+funexp(data.loc[month,'day'],data.loc[month,'day'],data.loc[month,'日导量'],1.8,b,c,1)-sy.exp(data['amount'][:month+1].sum())
            eq = eq + funexp(data.loc[month, 'day'], data.loc[month, 'day'], data.loc[month, '日导量'], 1.8, b, c,1) - 2.718**data['amount'][:month + 1].sum()
            eqList.append(sy.simplify(eq))
            print(sy.simplify(eq))

    print(len(eqList))
    print(eqList)
    result=sy.solve(eqList,[a,c])
    print(result)
    # y2 = [fun(i, -6, 1, 1) for i in range(1, 120)]
    # plt.plot(range(1, 120), y2, 'r--')
    plt.show()
    # print(sy.solve(eqList,[base,a,b,c]))