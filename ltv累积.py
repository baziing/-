import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import math
import sympy as sy
from scipy.optimize import root,fsolve
import matplotlib.pyplot as plt

# def func(x,a1,b1,a2,b2):
#     return a1*sy.exp(-b1*x)+a2*sy.exp(-b2*x)+1

def func(x,a1,b1,a2,b2,c):
    return a1*sy.exp(-b1*x)+a2*sy.exp(-b2*x)+c

def fund(x,a,b,c,d,e):
    return a*x**4+b*x**3+c*x**2+d*x+e

def fun(x,a,b):
    return x*(a*2)+b*3-2

def funltv(x,a1,b1,a2,b2,c):
    # ltv=1
    # for i in range(1,x+1):
    #     if i==1:
    #         ltv=1
    #     else:
    #         ltv=ltv*func(i,a1,b1,a2,b2,c)
    return fund(x,a1,b1,a2,b2,c)

if __name__ == '__main__':
    # a,b=sy.symbols("x y")
    # eq=[fun(1,a,b)-10,fun(2,a,b)-1]
    # result=sy.nonlinsolve(eq,[a,b])
    # print(list(result))
    a,b,c,d,e=sy.symbols("a b c d e")
    data = pd.read_csv('test.csv')
    data['日导量']=data['n']/data['day']
    eqList=[]
    for month in range(0,data.shape[0]-2):
        if month==0:
            sum=0
            for day in range(1,data.loc[month,'day']+1):
                sum=funltv(day,a,b,c,d,e)+sum
            eq=sum*data.loc[month,'日导量']/data.loc[month,'day']-data.loc[month,'amount']
            eqList.append(eq)
        else:
            eq=0
            for i in range(0,month):
                print(i,month)
                maxday=0
                sum=0
                for j in range(i,month+1):
                    maxday=data.loc[j,'day']+maxday
                print(maxday)
                for day in range(maxday-data.loc[i,'day'],maxday+1):
                    sum = funltv(day,a,b,c,d,e) + sum
                eq=sum*data.loc[i,'日导量']/data.loc[i,'day']+eq
            sum=0
            for day in range(1,data.loc[month,'day']+1):
                sum = funltv(day,a,b,c,d,e) + sum
            eq = eq+sum * data.loc[month, '日导量'] / data.loc[month, 'day'] - data.loc[month, 'amount']
            eqList.append(eq)
    eqList.append(funltv(1,a,b,c,d,e)-5)

    print(eqList)
    print(eqList)
    result = sy.solve(eqList, [a,b,c,d,e])
    # result = sy.nsolve(eqList, [base, a, b],[0.34,2.26,0.45])
    print(result)
    # print(result[3])
    y2 = [fund(i, result[a], result[b], result[c], result[d], result[e]) for i in range(1, 120)]
    plt.plot(range(1, 120), y2, 'r--')
    plt.show()
    # print(data)