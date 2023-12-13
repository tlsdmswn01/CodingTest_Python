def solution(left, right):
    new=0
    for i in range(left,right+1):
        answer = 0
        for k in range(1,i+1):
            if i%k==0:
                answer+=1
            else:
                pass
        if answer%2==0:
            new+=i
        else:
            new-=i
    return new