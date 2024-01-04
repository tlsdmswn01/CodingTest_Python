def solution(s):
    answer = []
    a=''
    count=0
    num=0
    while s!='1':
        count+=s.count('0')
        s=s.replace('0','')
        s=bin(len(s))[2:]
        num+=1
        
    answer.append(num)
    answer.append(count)
    return answer