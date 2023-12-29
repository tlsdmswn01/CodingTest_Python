def solution(array, commands):
    answer = []
    for o in commands:
        i,j,k=o[0],o[1],o[2]
        a=array[i-1:j]
        a.sort()
        answer.append(a[k-1])
    return answer