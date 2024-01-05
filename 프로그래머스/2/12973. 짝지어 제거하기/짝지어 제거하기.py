def solution(s):
# 답안 작성 부분 ===============

    a=[]
    for i in s:
        if not a:
            a.append(i)
        elif a[-1]==i:
            a.pop()
        else:
            a.append(i)

    if len(a)==0:
        return 1
    else:
        return 0