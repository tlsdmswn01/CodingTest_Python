def solution(arr):
    answer = 0
    b=1
    for k in arr:
        b*=k
    for i in range(max(arr),b+1):
        c=True
        for j in arr:
            if i%j==0:
                c=True
            else:
                c=False
                break
        if c:
            return i