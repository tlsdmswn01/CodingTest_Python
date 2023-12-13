def solution(arr):
    answer = []
    a=min(arr)
    if len(arr)>1:
        arr.remove(a)
        return arr
    else:
        return [-1]