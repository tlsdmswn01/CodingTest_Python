def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if i==k:
                continue
            answer.append(numbers[i]*numbers[k])
        
    return max(answer)