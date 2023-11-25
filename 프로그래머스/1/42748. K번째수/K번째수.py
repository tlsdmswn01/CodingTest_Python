def solution(array, commands):
    answer = []
    for i in commands:
        a,b,c=i[0],i[1],i[2]
        g=array[a-1:b]
        g.sort()
        answer.append(g[c-1])
    return answer