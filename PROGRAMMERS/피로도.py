from itertools import permutations
def solution(k, dungeons):
    value=0
    for x in list(permutations(dungeons,len(dungeons))):
        hp,tmp=k,0
        for i in x:
            if hp>=i[0]:
                hp-=i[1]
                tmp+=1
            else:
                break
        value=max(value,tmp)

    return value

# 경우의 수를 활용한 완탐