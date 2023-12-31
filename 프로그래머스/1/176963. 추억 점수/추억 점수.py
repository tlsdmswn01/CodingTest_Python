def solution(name, yearning, photo):
    answer = []
    a=0
    dic={}
    for i in range(len(name)):
        dic[name[i]]=yearning[i]
    for k in photo:
        a=0
        for j in k:
            try:
                a+=dic[j]
            except:
                a+=0
        answer.append(a)
    return answer