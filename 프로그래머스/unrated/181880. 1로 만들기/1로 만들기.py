def solution(num_list):
    a=0
    for i in num_list:
        while i!=1:
            if i%2==0:
                i//=2
                a+=1
            else:
                i-=1
                i//=2
                a+=1
    return a