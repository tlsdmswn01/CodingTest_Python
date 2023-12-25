def solution(arr):
    a=[arr[0]]
    for i in arr[1:]:
        b=a[-1]
        if b!=i:
            a.append(i)
        else:
            pass
    return a