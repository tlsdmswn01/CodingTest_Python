def solution(arr):
    answer = []
    a=0
    for i in arr:
        if not answer:
            answer.append(i)
            
        if answer[a]!=i:
            answer.append(i)
            a+=1
    return answer