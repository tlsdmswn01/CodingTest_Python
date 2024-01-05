def solution(n):
# 답안 작성 부분 ===============


    a=0
    b=0
    answer=0
    while a!=n:
        a+=1
        b=0
        for i in range(a,n+1):
            b+=i
            if b==n:
                answer+=1
                break
            elif b>n:
                break


# ==============================
    return answer