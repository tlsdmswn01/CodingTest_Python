def solution(ineq, eq, n, m):
    answer=0
    n=str(n)
    m=str(m)
    if eq=='=':
        if eval(n+ineq+eq+m):
            answer=1

    elif eq=='!':
        if eval(n+ineq+m):
            answer=1

    return answer