from bisect import bisect_left
from itertools import combinations


def solution(infos, queries):
    d = {}
    answer = []
    for info in infos:
        req = info.split(" ")
        myKey = req[:-1]
        myValue = req[-1]
        for i in range(len(myKey)+1):
            for c in list(combinations(myKey, i)):
                tmp = ''.join(c)
                if tmp in d:
                    d[tmp].append(int(myValue))
                else:
                    d[tmp] = [int(myValue)] # 해쉬의 value 값을 리스트형으로 추가
    for i in d:
        d[i].sort()
    for query in queries:
        qu = query.split(' ')
        quKey = qu[:-1]
        quValue = qu[-1]
        quKey = ''.join(quKey).replace("and", "").replace("-", "").replace(" ", "") # quKey의 and, -, 공백문자 제거
        if quKey in d:
            scores = d[quKey]
            if scores:
                answer.append(len(scores) - bisect_left(scores, int(quValue)))
        else:
            answer.append(0)
    return answer

# 시간 효율성을 위해 이분탐색, 해쉬 사용
# 해쉬의 val 값을 리스트 형으로 사용
# 정렬된 리스트에서 특정값(quValue)보다 큰 값이 몇 개있는지 counting하기 위해 이분탐색 활용