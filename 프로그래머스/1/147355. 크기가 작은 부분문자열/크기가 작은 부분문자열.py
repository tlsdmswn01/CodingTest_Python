def solution(t, p):
    answer = 0
    a=[]
    b=len(p)
    c=int(p)
    for i in range(0,len(t)):
        if len(t[i:i+b])==b:
            a.append(t[i:i+b])
    
    for k in a:
        if int(k)<=c:
            answer+=1
    return answer