import pandas as pd
import datetime
import time
import sympy as sy
from scipy.optimize import root
import matplotlib.pyplot as plt

def ltvmodel1(x,a,b,c):
    return a*sy.log(b*(x+c))

def ltvmodel2(x,a,b):
    return a*sy.log(b*x)

def ltvmodel3(x,a,b):
    return a/(x+b)

def ltvmodel4(x,a,b):
    return a/(x+b)**2

# begin开始计算的时间
# end结束时间
def ltvsum(begin,end,n,a,b,c):
    if begin==1:
        sum=ltvmodel1(end,a,b,c)
    else:
        sum=ltvmodel1(end,a,b,c)-ltvmodel1(begin-1,a,b,c)
    return sum*n

# 差值模型-累计时间段内玩家产生的价值
def ltvdiff(begin,end,n,a,b,model):
    sum=0
    for i in range(begin,end+1):
        if model==2:
            sum=sum+ltvmodel2(i,a,b)
        elif model==3:
            sum=sum+ltvmodel3(i,a,b)
        else:
            print('程序错误')
    return sum*n

def solvefun(unsolved_value):
    a,b=unsolved_value[0], unsolved_value[1]
    for i in range(0,len(eqs)):
        eqs[i]=eval(eqs[i])
    print(eqs)
    # meqList = [eval(str(eq)) for eq in eqList]
    return eqs

def create():
    global eqs
    eqs=[]
    # print(eqList[0])
    eqs.append(str(eqList[0]))
    eqs.append(str(eqList[1]))

if __name__ == '__main__':
    # 数据预处理
    data = pd.read_excel('ltv预测v0.xlsx', usecols=[1, 2, 3], names=['day', 'ppl', 'amount'])
    data = data[~data['day'].isin(['日期'])].reset_index(drop=True)
    data['day'] = data['day'].apply(lambda x: x.strftime('%Y-%m-%d'))
    data['amount'] = data['amount'] / 1000000
    data['ppl'] = data['ppl'] / 1000000
    # print(data)

    # 设定未知数
    a,b=sy.symbols('a b')

    # 7-30 绝对值
    # p=20
    # values=[(1,40),(1,60)]
    # eqList=[]
    # for value in values:
    #     sum=0
    #     for i in range(0,value[1]):
    #         print(1,i)
    #         sum=sum+ltvsum(value[0]-i if value[0]-i>0 else 1,value[1]-i,data.loc[i,'ppl'],a,b,p)
    #     eqList.append(sy.simplify(sum-data['amount'][value[0]-1:value[1]].sum()))
    # result1 = list(sy.nonlinsolve(eqList, [a, b]))
    # print(result1)

    ltvsumList=[]
    pList=[]
    values = [(1, 40), (1, 60)]
    for p in [20,40,60,80,100]:
        eqList = []
        for value in values:
            sum = 0
            for i in range(0, value[1]):
                print(1, p,i)
                sum = sum + ltvsum(value[0] - i if value[0] - i > 0 else 1, value[1] - i, data.loc[i, 'ppl'], a, b, p)
            eqList.append(sy.simplify(sum - data['amount'][value[0] - 1:value[1]].sum()))
        result1 = list(sy.nonlinsolve(eqList, [a, b]))
        if ltvmodel1(2,result1[0][0],result1[0][1],p)<=0:
            continue
        ltvsumList.append([ltvmodel1(i,result1[0][0],result1[0][1],p)for i in range(1,31)])
        pList.append(p)

    # 30-60 增量
    values=[(1,90),(1,180)]
    model=2
    eqList=[]
    for value in values:
        sum=0
        for i in range(0,value[1]):
            print(2,i)
            sum=sum+ltvdiff(value[0]-i if value[0]-i>0 else 1,value[1]-i,data.loc[i,'ppl'],a,b,model)
            # print(ltvdiff(value[0]-i if value[0]-i>0 else 1,value[1]-i,data.loc[i,'ppl'],a,b,model))
        eqList.append(sy.simplify(sum-data['amount'][value[0]-1:value[1]].sum()))
    result2 = list(sy.nonlinsolve(eqList, [a, b]))
    print(result2)

    # >60 增量
    # values=[(1,90),(1,45)]
    # model=3
    # eqList=[]
    # for value in values:
    #     sum=0
    #     for i in range(0,value[1]):
    #         sum=sum+ltvdiff(value[0]-i if value[0]-i>0 else 1,value[1]-i,data.loc[i,'ppl'],a,b,model)
    #     eqList.append(sy.simplify(sum-data['amount'][value[0]-1:value[1]].sum()))
    # print(eqList)
    result3=[2.18732436, 5.02223993]
    # result = sy.nonlinsolve(eqList, [a, b])
    # print(result)
    # eqList=[]
    # eqList.append(a+b-3)
    # eqList.append(b-a+2)
    # testList=[1,1]
    # create()
    # solved = root(solvefun, testList)
    # print(solved)

    ltvList=[]
    color=['b','g','c','m','y']
    for j in range(0,len(ltvsumList)):
        ltvList=ltvsumList[j]
        # ltvList.append(ltv0)
        for i in range(31,181):
            if i<=50:
                ltvList.append(ltvList[-1] + ltvmodel2(i, result2[0][0], result2[0][1]))
            elif i<=90:
                ltvList.append(ltvList[-1] + ltvmodel3(i, result3[0], result3[1]))
            else:
                ltvList.append(ltvList[-1] + ltvmodel3(i, result3[0], result3[1]))
                # ltvList.append(ltvList[-1] + ltvmodel4(i, 415.10563042, 43.3586688))
        plt.plot(range(1, 181), ltvList, color[j]+'--',label=pList[j])

    # plt.show()


    # for i in range(1,181):
    #     if i<=30:
    #         ltvList.append(ltvmodel1(i,result1[0][0],result1[0][1],p))
    #     elif i<=50:
    #         print(ltvmodel2(i,result2[0][0],result2[0][1]))
    #         ltvList.append(ltvList[-1]+ltvmodel2(i,result2[0][0],result2[0][1]))
    #     elif i<=90:
    #         print(ltvmodel3(i,result3[0],result3[1]))
    #         ltvList.append(ltvList[-1]+ltvmodel3(i,result3[0],result3[1]))
    #     else:
    #         ltvList.append(ltvList[-1] + ltvmodel4(i,415.10563042,  43.3586688))
    # print(ltvList)

    # plt.plot(range(1, 181), ltvList, 'g--')

    for i in range(0,len(ltvList)):
        print(round(ltvList[i],2))

    df=pd.read_csv('../data/ltv.csv')
    plt.plot(range(1,181),df['ltv'][0:180].tolist(),'r',label='real')
    plt.legend()
    plt.show()