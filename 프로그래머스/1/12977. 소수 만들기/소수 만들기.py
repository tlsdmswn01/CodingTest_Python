def solution(nums):
    answer = 0
    l=len(nums)
    b=[]
    for i in range(l):
        for k in range(i+1,l):
            for j in range(k+1,l):
                a=nums[i]+nums[k]+nums[j]
                b.append(a)
    
    for u in b:
        p=True
        
        for h in range(2,u):
            if u%h==0:
                p=False
        
        if p:
            answer+=1
    return answer