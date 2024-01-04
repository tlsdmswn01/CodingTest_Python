def solution(s):
    answer = []
    a=0
    c=0
    while s!='1':
        a+=s.count('0')
        s=s.replace('0','')
        s=bin(len(s))[2:]
        c+=1

    answer.append(c)
    answer.append(a)
    return answer