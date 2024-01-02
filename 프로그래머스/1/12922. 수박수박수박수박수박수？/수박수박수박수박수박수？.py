def solution(n):
# 답안 작성 부분 ===============
    answer=''
    a=0
    while a!=n:
        for i in '수박':
            answer+=i
            a+=1
            if a==n:
                break
        
# ==============================
    return answer