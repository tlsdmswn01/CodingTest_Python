from collections import deque
def solution(numbers, direction):
    
    answer=deque(numbers)
    if direction=='right':
        answer.rotate(1)
    if direction =='left':
        answer.rotate(-1)
    
    return list(answer)
