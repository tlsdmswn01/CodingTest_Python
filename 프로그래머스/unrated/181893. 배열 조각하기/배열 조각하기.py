def solution(arr, query):
    answer = []
    for i,k in enumerate(query):
        if not answer:
            if i%2==0:
                answer.extend(arr[:k+1])
            else:
                answer.extend(arr[k:])
        else:
            if i%2==0:
                answer=answer[:k+1]
            else:
                answer=answer[k:]
    return answer