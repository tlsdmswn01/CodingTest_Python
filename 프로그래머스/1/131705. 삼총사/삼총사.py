def solution(number):
    answer=0
    k=len(number)
    for i in range(k):
        for j in range(i+1,k):
            for u in range(j+1,k):
                if number[i]+number[j]+number[u]==0:
                    answer+=1
    return answer