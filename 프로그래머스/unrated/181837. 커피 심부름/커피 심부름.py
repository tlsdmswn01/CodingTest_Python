def solution(order):
    result=0
    for i in order:
        if 'latte' in i:
            result+=5000
        elif 'americano' in i:
            result+=4500
        elif 'anything' in i:
            result+=4500
    return result