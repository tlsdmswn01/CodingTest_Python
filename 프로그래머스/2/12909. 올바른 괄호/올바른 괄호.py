
def solution(s):
# 답안 작성 부분 ===============
    a=0
    for i in s:
        if i=='(':
            a+=1
        else:
            a-=1
        if a<0:
            return False
    if a>0:
        return False
    return True