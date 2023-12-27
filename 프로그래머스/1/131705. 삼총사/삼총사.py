def solution(number):
    answer = 0
    l=len(number)
    for i in range(l):
        for k in range(i+1,l):
            for j in range(k+1,l):
                if number[i]+number[k]+number[j]==0:
                    answer+=1
                    
                
    return answer