def solution(quiz):
    answer = []
    a=[]
    b=[]
    for i in quiz:
        b.extend(i.split()[-1:])
        a.append(eval(''.join(i.split()[:-2])))
    b=list(map(int,b))
    
    for k in range(len(a)):
        if a[k]==b[k]:
            answer.append('O')
        else:
            answer.append('X')
    return answer