import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import math
import sympy as sy
import matplotlib.pyplot as plt

def fun(x,a,b,c):
    return a*sy.exp(-b*x)+c

def taylor(x):
    n=5
    sum=0
    for i in range(0,n+1):
        sum=sum+((x)**i)/math.factorial(i)
    return sum

def funltv(x,a,b,c):
    return a*taylor(-b*x)+c

def amount(end,num,n,a,b,c):
    sum=0
    for i in range(end-num+1,end+1):
        sum=sum+funltv(i,a,b,c)
    return sum*n


if __name__ == '__main__':
    a,b,c=sy.symbols('a b c')

    data = pd.read_csv('../test.csv')
    data['日导量'] = data['n'] / data['day']
    eqList = []
    for month in range(0,3):
        print(month)
        if month==0:
            eq=amount(data.loc[month, 'day'],data.loc[month, 'day'],data.loc[month, '日导量'],a,b,c)-data.loc[month, 'amount']
            eqList.append(sy.simplify(eq))
            print(sy.simplify(eq))
        else:
            eq=0
            for i in range(0,month):
                maxday=data['day'][i:month+1].sum()
                eq=eq+amount(maxday,data.loc[i,'day'],data.loc[i,'日导量'],a,b,c)-data['amount'][:month + 1].sum()
            eqList.append(sy.simplify(eq))
            print(sy.simplify(eq))

    print(len(eqList))
    print(eqList)
    result = sy.nonlinsolve(eqList, [a,b,c])
    print(result)