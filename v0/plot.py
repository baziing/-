import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def funa(x,a,b):
    return a*np.log(b*x)

def funb(x,a,b):
    return a/(x+b)

def func(x,a,b):
    return a*np.log(b*(x+70))

def fund(x, a, b):
    return a * np.log(b * (x + 70))
    # return a*x**3+b*x+c
    # return a*np.log(b*(x+10))

# plt.plot(range(1,16),[funa(i,-0.164822608279469, 0.0434387571847647) for i in range(1,16)],'bs')
# plt.plot(range(1,60),[func(i,3.06180706308605, 0.0526268867069963) for i in range(1,60)],'b--')
# plt.plot(range(1,60),[fund(i,2.76423907589727, 0.0654706022302038) for i in range(1,60)],'g--')
plt.plot(range(1,60),[fund(i,8.66382454076878, 0.014679624179565) for i in range(1,60)],'g--')

# plt.plot(range(1,61),[funa(i,-0.0725266867195636, 0.00948097761710896) for i in range(1,61)],'b--')
# plt.plot(range(1,121),[funa(i,-0.0705939676013684, 0.00900909313289423) for i in range(1,121)],'b--')
# plt.plot(range(1,181),[funa(i,-0.0617481619690565, 0.00713508588689670) for i in range(1,181)],'b--')

# plt.plot(range(1,30),[func(i,3.19760414, 1.39500252, 0.13881366) for i in range(1,30)],'gs')
# plt.plot(range(1,16),[funb(i,1.64180238, 1.99279338) for i in range(1,16)],'gs')
# plt.plot(range(1,31),[funb(i,2.2874109 , 4.36926897) for i in range(1,31)],'g:')
# plt.plot(range(1,61),[funb(i,3.52593372, 10.2661868) for i in range(1,61)],'g:')
# plt.plot(range(1,121),[funb(i,2.47523897, 4.58265984) for i in range(1,121)],'g:')
# plt.plot(range(1,181),[funb(i,2.22428578, 2.94049228) for i in range(1,181)],'g:')

data = pd.read_csv('../data/test.csv')
mlist=data['add'][1:60].tolist()
plt.plot(range(1,60),mlist,'r')
# print([funa(i,-0.0617481619690565, 0.00713508588689670) for i in range(1,181)])
# print([funb(i,2.22428578, 2.94049228) for i in range(1,181)])
# print([funb(i,2.2874109 , 4.36926897) for i in range(1,31)])
print(mlist)
plt.show()

