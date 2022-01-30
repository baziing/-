import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import math
import sympy as sy
import matplotlib.pyplot as plt

def taylor(x):
    n=5
    sum=0
    for i in range(0,n+1):
        sum=sum+((x)**i)/math.factorial(i)
    return -1/sum
n=30
xdata=range(1,30)
y2 = [taylor(i) for i in xdata]
y3=[2.7**i for i in xdata]
print(y2)
print(y3)
plt.plot(xdata, y2, 'r--')
# plt.plot(xdata, y3, 'b--')
plt.show()