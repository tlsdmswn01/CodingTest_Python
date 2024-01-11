def solution(n):
    answer = 0
    pre=0
    current=1
    for i in range(n):
        pre,current=current,pre+current
    answer+=current%1234567
    return answer