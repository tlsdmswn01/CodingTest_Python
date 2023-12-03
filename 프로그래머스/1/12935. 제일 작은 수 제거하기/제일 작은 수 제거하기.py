def solution(arr):
    answer = []
    a=min(arr)
    arr.remove(a)
    if not arr:
        return [-1]
    else:
        return arr