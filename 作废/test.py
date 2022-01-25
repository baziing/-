import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import math
import sympy as sy
from scipy.optimize import root,fsolve

# def func(x,a1,b1,a2,b2):
#     return a1*sy.exp(-b1*x)+a2*sy.exp(-b2*x)+1

def func(x,a1,b1):
    return a1*sy.exp(-b1*x)+1

def fun(x,a,b):
    return x*(a*2)+b*3-2

def funltv(x,a1,b1):
    ltv=1
    for i in range(1,x+1):
        if i==1:
            ltv=1
        else:
            ltv=ltv*func(i,a1,b1)
    return ltv

if __name__ == '__main__':
    # a,b=sy.symbols("x y")
    # eq=[fun(1,a,b)-10,fun(2,a,b)-1]
    # result=sy.nonlinsolve(eq,[a,b])
    # print(list(result))
    base,a,b=sy.symbols("base a b")
    data = pd.read_csv('../test.csv')
    data['日导量']=data['n']/data['day']
    eqList=[]
    for month in range(0,data.shape[0]):
        if month==0:
            sum=0
            for day in range(1,data.loc[month,'day']+1):
                sum=funltv(day,a,b)+sum
            eq=base*(sum*data.loc[month,'日导量']/data.loc[month,'day'])-data.loc[month,'amount']
            eqList.append(eq)
        else:
            eq=0
            for i in range(0,month):
                print(i,month)
                maxday=0
                sum=0
                for j in range(i,month+1):
                    maxday=data.loc[j,'day']
                for day in range(maxday-data.loc[i,'day'],maxday+1):
                    sum = funltv(day, a, b) + sum
                eq=base*(sum*data.loc[i,'日导量']/data.loc[i,'day'])+eq
            sum=0
            for day in range(1,data.loc[month,'day']+1):
                sum = funltv(day, a, b) + sum
            eq = base * (sum * data.loc[month, '日导量'] / data.loc[month, 'day']) - data.loc[month, 'amount']
            eqList.append(eq)
    print(eqList[0])
    # result = sy.nsolve(eqList, [base,a,b],[1,2.264050514673929,0.4540032298870311])
    # result = sy.nsolve(eqList, [base, a, b],[0.34,2.26,0.45])
    # print(list(result))
    print(data)