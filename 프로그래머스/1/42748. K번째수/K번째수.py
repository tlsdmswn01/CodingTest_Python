def solution(array, commands):
# 답안 작성 부분 ===============
    answer=[]
    for i in commands:
        a,b,c=i[0],i[1],i[2]
        d=array[a-1:b]
        d.sort()
        answer.append(d[c-1])

# ==============================
    return answer