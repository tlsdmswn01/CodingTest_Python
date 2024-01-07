def solution(answers):
    answer = []
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    score1,score2,score3=0,0,0
    
    for i in range(len(answers)):
        if len(answers)> len(num3):
            num1=num1*len(answers)*2
            num2=num2*len(answers)*2
            num3=num3*len(answers)*2
            
        if answers[i]==num1[i]:
            score1+=1
        if answers[i]==num2[i]:
            score2+=1
        if answers[i]==num3[i]:
            score3+=1
    a=[score1,score2,score3]
    b=max(a)
    for j,h in enumerate(a):
        if h==b:
            answer.append(j+1)

    return answer
