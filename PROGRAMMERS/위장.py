def solution(clothes):
    info={}
    for i in range(len(clothes)):
        if clothes[i][1] in info.keys():
            info[clothes[i][1]]+=1
        else:
            info[clothes[i][1]]=1
    answer = 1
    for i in info.values():
        answer*=i+1
    return answer-1

# 백준-패션왕 신혜빈과 동일한 문제
# headgear : {"yellowhat", "greenturban"}
# eyewear : {"eyewear"}
# (headgear의 개수 + 1) * (eyewear의 개수 + 1) - 1
# headgear : {"yellowhat", "greenturban", NULL} * {"eyewear", NULL} - (NULL,NULL인 경우의 수 = 1)