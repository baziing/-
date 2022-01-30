import pandas as pd
from scipy.optimize import root
import matplotlib.pyplot as plt
import numpy as np

test='2'

def ltvmodel0(x,a,b,p):
    return a*np.log(x+p)-np.exp(-x)+b


def ltvmodel1(x,a,b):
    return a/(x+b)**2


def ltvmodel2(x,a,b):
    return a/(x+b)


def ltvmodel3(x,a,b):
    return a/(np.log(x+b)+x)


def ltvmodel4(x,a,b):
    return a/np.log(x+b)


def ltvmodel(x,a,b,p):
    if 'A' in p or 'a' in p:
        p=int(float(p[1:]))
        return ltvmodel0(x,a,b,p)
    elif 'B' in p or 'b' in p:
        p=int(p[1:])
        if p==1:
            return ltvmodel1(x,a,b)
        elif p==2:
            return ltvmodel2(x,a,b)
        elif p==3:
            return ltvmodel3(x,a,b)
        elif p==4:
            return ltvmodel4(x,a,b)


def ltv(begin,end,n,a,b,p):
    sum=0
    if 'A' in p or 'a' in p:
        if begin==1:
            sum=ltvmodel(end,a,b,p)
        else:
            sum=ltvmodel(end,a,b,p)-ltvmodel(begin-1,a,b,p)
    elif 'B' in p or 'b' in p:
        sum=0
        for i in range(begin,end+1):
            # print(i,end)
            sum=sum+ltvmodel(i,a,b,p)
    return sum*n


def getModel(score):
    if score<0.4:
        return ['B2','B1']
    elif score<0.5:
        return ['B3','B2']
    elif score<0.7:
        return ['B4','B3']
    elif score>=0.7:
        return ['B4','B4']


def solve_function(unsolved_value):
    a, b = unsolved_value[0], unsolved_value[1]
    eqList=[]
    for value in values:
        sum = 0
        for i in range(0, value[1]):
            sum = sum + ltv(value[0] - i if value[0] - i > 0 else 1, value[1] - i, data.loc[i, 'ppl'], a, b, p)
        eqList.append(sum - data['amount'][value[0] - 1:value[1]].sum())
    return eqList


def getP(score):
    if score<=0.4:
        return round(-125*score+100)
    elif score<=0.5:
        return round(-300*score+170)
    elif score<=0.7:
        return round(-50*score+5)
    elif score>0.7:
        return round(100*(-score+1)/3)


def calmodel(score):
    mpList=[]
    mpList.append(abs(getP(score)))
    mlist = [1, 1]
    global p
    for mp in mpList:
        pList = []
        resultList = []
        p='A'+str(mp)
        pList.append(p)
        solved = root(solve_function, mlist)
        resultList.append(solved.x)

        p=getModel(score)[0]
        pList.append(p)
        solved = root(solve_function, mlist)
        resultList.append(solved.x)

        p=getModel(score)[1]
        pList.append(p)
        solved = root(solve_function, mlist)
        resultList.append(solved.x)

        drawing(pList,resultList)
        print(pList,resultList)
        plt.plot(range(1, 181), drawing(pList,resultList)[0:180], label=pList[0])

    df = pd.read_csv('../data/ltv.csv')
    plt.plot(range(1, 181), df['ltv'+test][0:180].tolist(), 'r', label='real')
    plt.legend()
    plt.show()


def drawing(pList,resultList):
    ltvList=[]
    for i in range(1,181):
        if i<=30:
            ltvList.append(ltvmodel(i,resultList[0][0],resultList[0][1],pList[0]))
        elif i<=60:
            ltvList.append(ltvList[-1]+ltvmodel(i,resultList[1][0],resultList[1][1],pList[1]))
        else:
            ltvList.append(ltvList[-1] + ltvmodel(i, resultList[2][0], resultList[2][1], pList[2]))
    print(str(ltvList).rstrip(']').lstrip('['))
    return ltvList


if __name__ == '__main__':
    data = pd.read_excel('ltv预测v'+test+'.xlsx', usecols=[1, 2, 3], names=['day', 'ppl', 'amount'])
    data = data[~data['day'].isin(['日期'])].reset_index(drop=True)
    data['day'] = data['day'].apply(lambda x: x.strftime('%Y-%m-%d'))
    data['amount'] = data['amount'] /1000000/100
    data['ppl'] = data['ppl'] / 1000000
    score = data['amount'][90:180].sum() / data['amount'][0:90].sum() - data['ppl'][90:180].sum() / data['ppl'][0:90].sum()
    values=[(1,90),(1,180)]
    print(score)
    calmodel(score)
    # plt.show()
    print('end------------------------------')