def solution(nums):
    answer = 0
    l=len(nums)
    for i in range(l):
        for k in range(i+1,l):
            for j in range(k+1,l):
                a=True
                b=nums[i]+nums[k]+nums[j]
                for h in range(2,b):
                    if b%h==0:
                        a=False
                        
                if a:
                    answer+=1
                
    return answer