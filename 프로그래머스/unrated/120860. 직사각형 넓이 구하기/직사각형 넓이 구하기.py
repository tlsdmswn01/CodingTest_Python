def solution(dots):
    a=[]
    b=[]
    for i in dots:
        a.append(i[0])
        b.append(i[1])
    answer= (max(a)-min(a))*(max(b)-min(b))
    
    return answer