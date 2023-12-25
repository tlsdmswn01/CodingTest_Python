def solution(n, m):
    answer = []  
    for i in range(max(m,n),m*n+1):
        if i%m==0 and i%n==0:
            answer.append(i)
            break
        
    if n>m:
        while n%m!=0:
                c=n%m
                n,m=m,c
        answer.append(m)
    else:
        while m%n!=0:
            c=m%n
            m,n=n,c
        answer.append(n)    
        
    answer.sort()
    return answer