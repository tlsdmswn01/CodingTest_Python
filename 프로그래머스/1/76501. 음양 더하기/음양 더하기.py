def solution(absolutes, signs):
    answer=0
    for i in range(len(signs)):
        if signs[i]:
            answer+=absolutes[i]
            continue
        answer-=absolutes[i]
    return answer