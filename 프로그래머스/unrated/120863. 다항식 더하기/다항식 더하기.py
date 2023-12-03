def solution(polynomial):
    a=[]
    b=0
    s=polynomial.split()
    for i in s:
        if 'x' in i:
            a.append(i)
        elif i.isdigit():
             b+=int(i)
    c=[]            
    for k in a:
        k=k.replace('x','')
        if k=='':
            c.append(1)
        else:
            c.append(int(k))
    print(c)
            
    if len(c)==0:
        return str(b)
    if b!=0:
        if len(c)==1 and c[0]==1:
            return 'x + '+str(b)
        else: 
            return str(sum(c))+'x + '+str(b)
    elif b==0:
        if len(c)==1 and c[0]==1:
            return 'x'
        else:
            return str(sum(c))+'x'
