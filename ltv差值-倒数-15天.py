import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import math
import sympy as sy
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import root
import numpy as np


def fun(x,a,b,c):
    # return a*2.718**(-b*x)+c
    # return a *sy.log(b * x)
    return a/(x+b)**2

def ltv(end,day,n,a,b,c):
    sum=0
    for i in range(end-day,end+1):
        if i<1:
            continue
        sum=fun(i,a,b,c)+sum
    sum=sum*n
    return sum

def shishi():
    global eq1
    eq1 = []
    eq1.append(str(14.847*a/(b + 5) + 33.1643*a/(b + 4) + 42.1149*a/(b + 3) + 50.6288*a/(b + 2) + 59.448*a/(b + 1) - 60.824133))
    eq1.append(str(14.847*a/(b + 10) + 33.1643*a/(b + 9) + 42.1149*a/(b + 8) + 50.6288*a/(b + 7) + 59.448*a/(b + 6) + 66.5638*a/(b + 5) + 71.5632*a/(b + 4) + 76.2871*a/(b + 3) + 81.1767*a/(b + 2) + 85.4427*a/(b + 1) - 128.215963))

def solve_function(unsolved_value):
    a, b= unsolved_value[0], unsolved_value[1]
    for i in range(0,len(eq1)):
        eq1[i]=eval(eq1[i])
    print(eq1)
    return eq1

if __name__ == '__main__':
    data = pd.read_csv('esm.csv')
    data['amount'] = data['amount']/100/10000
    data['ppl'] = data['ppl']/10000
    print(data)

    a, b,c= sy.symbols("a b c")
    eqList = []

    sum=0
    date=180
    for i in range(0,date):
        print(1,i)
        sum=sum+ltv(date-i,date,data.loc[i,'ppl'],a,b,c)
    sum=sum-data['amount'][0:date].sum()
    eqList.append(sum)
    print(eqList[-1])

    sum = 0
    date = 90
    for i in range(0, date):
        print(2,i)
        sum = sum + ltv(date - i, date, data.loc[i, 'ppl'], a, b, c)
    sum = sum - data['amount'][0:date].sum()
    eqList.append(sum)
    print(eqList[-1])

    # sum = 0
    # date = 15
    # for i in range(0, date):
    #     sum = sum + ltv(date - i,date, data.loc[i, 'ppl'], a, b, c)
    # sum = sum - data['amount'][0:date].sum()
    # eqList.append(sy.simplify(sum))
    # print(eqList[-1])

    print(eqList)
    # result = sy.solve(eqList, [a, b])
    # print(result)

    # shishi()
    #
    # print(1)
    # list1 = [1, 1]
    # solved = root(solve_function, list1)
    # print(solved)
