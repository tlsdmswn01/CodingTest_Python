def solution(s):
    answer = []
    result=[]
    for i in s:
        answer.append(i)
        if answer.count(i)==1:
            result.append(-1)
        else:
            a=0
            for k in range(len(answer)-1,0,-1):
                a+=1
                if answer[len(answer)-1]==answer[len(answer)-1-a]:
                    break
            result.append(a)
            
    return result