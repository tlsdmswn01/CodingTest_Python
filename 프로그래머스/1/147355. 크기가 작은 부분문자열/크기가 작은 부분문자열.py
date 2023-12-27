def solution(t, p):
    answer = 0
    a=[]
    l=len(p)
    for i in range(0,len(t)):
        if len(t[i:i+l])==l:
            a.append(t[i:i+l])
            
    for i in a:
        if int(i)<=int(p):
            answer+=1
    return answer