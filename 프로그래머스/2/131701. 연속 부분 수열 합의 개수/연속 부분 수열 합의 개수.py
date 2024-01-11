def solution(elements):
    answer = 0
    c=set()
    elementslen=len(elements)
    elements=elements*2
    for i in range(elementslen):
        for j in range(elementslen):
            c.add(sum(elements[j:j+i+1]))
    return len(c)