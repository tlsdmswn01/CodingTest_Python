def solution(a, b, n):
    answer = 0
    while n>=a:
        c=0
        for i in range(n,0,-1):
            if i%a==0:
                c=i
                break
        get=(c//a)*b
        answer+=get
        n=n-c+get
    return answer