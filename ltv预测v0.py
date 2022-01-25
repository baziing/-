import pandas as pd
import datetime
import time
import sympy as sy

def ltvmodel1(x,a,b,c):
    return a*sy.log(b*(x+c))

def ltvmodel2(x,a,b):
    return a*sy.log(b*x)

def ltvmodel3(x,a,b):
    return a/(x+b)

# end表示截止时间
# day表示时间段跨度
def ltvsum(end,day,n,a,b,c):
    sum=ltvmodel1(end,a,b,c)-ltvmodel1(end-day)
    return sum*n

# 差值模型-累计时间段内玩家产生的价值
# end表示计算截止时间
# day表示同批数据的跨度
def ltvdiff(end,day,n,a,b,model):
    sum=0
    for i in range(end-day,end+1):
        if i<1:
            continue
        if model==2:
            sum=sum+ltvmodel2(i,a,b)
        elif model==3:
            sum=sum+ltvmodel3(i,a,b)
        else:
            print('程序错误')
    return sum*n

if __name__ == '__main__':
    # 数据预处理
    data = pd.read_excel('ltv预测v0.xlsx', usecols=[1, 2, 3], names=['day', 'ppl', 'amount'])
    data = data[~data['day'].isin(['日期'])].reset_index(drop=True)
    data['day'] = data['day'].apply(lambda x: x.strftime('%Y-%m-%d'))
    print(data)