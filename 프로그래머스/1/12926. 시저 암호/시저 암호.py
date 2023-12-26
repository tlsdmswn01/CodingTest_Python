def solution(s, n):
    answer = ''
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b='abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i in b:
            answer+=b[(b.index(i)+n)%26]
        elif i in a:
            answer+=a[(a.index(i)+n)%26]
        else:
            answer+=i
        

    return answer