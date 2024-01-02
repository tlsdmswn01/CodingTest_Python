def solution(d, budget):
    answer = 0
    d.sort()
    for idx,cost in enumerate(d):
        budget-=cost
        if budget<0:
            return idx
    return len(d)