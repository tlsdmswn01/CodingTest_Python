def solution(k, m, score):
    score.sort()
    c=[]
    while len(score)>=m:
        b=[]
        for i in range(m):
            a=score.pop()
            b.append(a)
        c.append(b)
    
    answer=0
    for k in c:
        answer+=min(k)*m
    return answer