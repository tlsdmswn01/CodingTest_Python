def solution(nums):
    answer = 0
    a=len(set(nums))
    if len(nums)/2 > a:
        return a
    else:
        return len(nums)/2
    return answer