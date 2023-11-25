from math import gcd
def factorization(x):
    d=2
    output=[]
    while d<=x:
        if x%d==0:
            output.append(d)
            x/=d
        else:
            d+=1
    return output

def solution(a,b):
    divide_num=gcd(a,b)
    result = b//divide_num
    for num in factorization(result):
        if num not in [2,5]:
            return 2
    return 1