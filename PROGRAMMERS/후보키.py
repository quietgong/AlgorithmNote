from itertools import combinations
def solution(relation):
    row=len(relation)
    col=len(relation[0])

    candidate=[]
    for i in range(1,col+1):
        candidate.extend(combinations(range(col),i))

    unique=[]
    for candi in candidate:
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(tmp))==row:
            flag=True

            for x in unique:
                if set(x).issubset(set(candi)):
                    flag=False
            if flag:
                unique.append(candi)

    return len(unique)

# append, extend 차이
# 컴프리헨션
# issubset
# 튜플, 집합 공부