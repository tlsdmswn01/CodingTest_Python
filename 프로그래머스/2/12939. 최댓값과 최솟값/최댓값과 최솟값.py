def solution(s):
    answer = ''
    a=list(map(int,s.split(' ')))
    a.sort()
    c,d=str(a[0]),str(a[-1])
    return c+' '+d