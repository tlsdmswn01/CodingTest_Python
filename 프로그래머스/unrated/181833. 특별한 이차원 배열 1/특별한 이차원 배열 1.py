def solution(n):
    arr=[]
    for i in range(n):
        arr.append([]) 
        for j in range(n):
            arr[i].append(0) 
    for i in range(n):
        for j in range(n):
            if i==j:
                arr[i][j]=1
            else:
                arr[i][j]=0
    return arr