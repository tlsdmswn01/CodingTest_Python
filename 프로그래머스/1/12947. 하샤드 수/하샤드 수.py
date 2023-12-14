def solution(x):
    answer=True
    a=sum(list(map(int,str(x))))
    if x%a==0:
        answer=True
    else:
        answer=False




# ==============================
    return answer
