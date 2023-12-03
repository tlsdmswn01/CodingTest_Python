def solution(num, total):
    avg=total//num
    a=[]
    for i in range(avg - (num-1)//2,avg+(num+2)//2):
        a.append(i)
    return a