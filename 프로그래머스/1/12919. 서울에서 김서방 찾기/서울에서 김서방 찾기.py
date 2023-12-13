def solution(seoul):
    answer = ''
    if 'Kim' in seoul:
        return '김서방은 {}에 있다'.format(seoul.index('Kim'))