def solution(numbers):
    answer = []
    l=len(numbers)
    for k in range(l):
        for j in range(k+1,l):
            answer.append(numbers[k]+numbers[j])
    a=list(set(answer))
    a.sort()
    return a