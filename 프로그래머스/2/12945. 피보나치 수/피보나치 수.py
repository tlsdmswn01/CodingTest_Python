def solution(n):
# 답안 작성 부분 ===============
    a=0
    b=1
    for i in range(2,n+1):
        a, b= a+b,a
    return (a+b)%1234567