def solution(arr1, arr2):
    answer = []
    for i,j in enumerate(arr1):
        answer.append([])
        for k in range(len(j)):
            answer[i].append(arr1[i][k]+arr2[i][k])
    return answer