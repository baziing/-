from scipy.optimize import root
import sympy as sy
import pandas as pd

def fun(x,a,b,c):
    return a*sy.log(b*x)
    # return a*(x-b)**5
    # return a/(x+b)
    # return a*1.5**(b*x)
    # return a*sy.log(b/x)
    # return a*sy.log(x)+b

def ltv1(begin,end,data,a,b,c):
    all=0
    for day in range(0,end):
        sum=0
        for i in range(begin-day,end-day+1):
            if i<1:
                continue
            else:
                print(day,i,fun(i, a, b, c))
                sum = sum + fun(i, a, b, c)
        all=all+sum*data.loc[day,'ppl']
    return all

def duoxiangshi():
    data = pd.read_csv('test.csv')
    data['amount'] = data['amount'] / 100 / 10000
    data['ppl'] = data['ppl'] / 10000

    a, b, c = sy.symbols("a b c")

    eqList=[]
    begin=0
    end=90
    print(end/2)
    # eqList.append(sy.simplify(ltv1(begin,5, data, a, b, 1) - data['amount'][begin:5].sum()))
    # print(eqList[-1])
    eqList.append(sy.simplify(ltv1(begin,int(end/2), data, a, b, 2) - data['amount'][begin:int(end/2)].sum()))
    print(eqList[-1])
    eqList.append(sy.simplify(ltv1(begin,end, data, a, b, 2) - data['amount'][begin:end].sum( )))

    print(len(eqList))
    print(eqList)
    result = sy.solve(eqList, [a, b])
    print(result)

    return

if __name__ == '__main__':
    duoxiangshi()
    print('end')