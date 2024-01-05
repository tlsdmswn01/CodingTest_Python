def solution(nums):
    if (len(nums)//2) > len(set(nums)):
        return int(len(set(nums)))
    else:
        return int(len(nums)/2)