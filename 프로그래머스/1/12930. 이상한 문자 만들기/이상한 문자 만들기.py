def solution(s):
    answer = []
    for i in s.split(' '):
        i=list(i)
        print(i)
        for k in range(len(i)):
            if k%2==0 or k==0:
                i[k]=i[k].upper()
            else:
                i[k]=i[k].lower()
        answer.append(''.join(i))
    return ' '.join(answer)