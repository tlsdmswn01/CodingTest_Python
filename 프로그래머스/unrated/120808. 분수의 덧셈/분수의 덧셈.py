from math import gcd
def solution(numer1, denom1, numer2, denom2):
    answer = []
    a=numer1*denom2+numer2*denom1
    b= denom1*denom2
    divide=gcd(a,b)
    answer.append(a/divide)
    answer.append(b/divide)
    
    
    return answer