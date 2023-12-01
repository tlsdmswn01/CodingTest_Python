def solution(n): # 피자는 6조각
    answer = 0
    a=1
    while (6*a)%n!=0:
        a+=1
        answer+=1
    answer+=1
    return answer