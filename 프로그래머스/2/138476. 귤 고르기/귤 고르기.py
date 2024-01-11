def solution(k, tangerine):
    answer = 0
    a={}
    for i in tangerine:
        try:
            a[i]+=1
        except:
            a[i]=1
    a=sorted(a.items(), key=lambda x: (x[1],x[0]),reverse=True)
    
    c=[]
    for h,j in a:
        for o in range(j):
            c.append(h)
            if len(c)==k:
                break
        if len(c)==k:
            break
                
    return len(list(set(c)))   