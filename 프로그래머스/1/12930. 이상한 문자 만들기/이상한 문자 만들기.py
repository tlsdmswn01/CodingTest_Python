def solution(s):
# 답안 작성 부분 ===============
    answer=[]
    for i in s.split(' '):
        i=list(i)
        for k in range(len(i)):
            if k==0 or k%2==0:
                i[k]=i[k].upper()
            else:
                i[k]=i[k].lower()
        answer.append(''.join(i))

# ==============================
    return ' '.join(answer)