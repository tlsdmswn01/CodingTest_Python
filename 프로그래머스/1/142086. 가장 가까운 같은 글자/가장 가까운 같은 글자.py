def solution(s):
    a=[]
    answer=[]
    for i in s:
        c=0
        a.append(i)
        if a.count(i)==1:
            answer.append(-1)
            continue
        else:
            for k in range(len(a)-1,0,-1):
                c+=1
                if a[len(a)-1]==a[len(a)-1-c]:
                    break
            answer.append(c)
    return answer