def solution(elements):
    a=set()
    l=len(elements)
    elements=elements*2
    for i in range(l):
        for j in range(l):
            a.add(sum(elements[i:i+j+1]))
    return len(list(a))