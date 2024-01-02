
def solution(arr):
# 답안 작성 부분 ===============
    answer=[arr[0]]
    for i in range(1,len(arr)):
        if answer[-1]!=arr[i]:
            answer.append(arr[i])
        else:
            pass
            
# ==============================
    return answer