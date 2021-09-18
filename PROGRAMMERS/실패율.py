def solution(N, stages):
    ans=[]
    person_num=len(stages)
    for i in range(1,N+1):
        if person_num==0:
            ans.append((i, 0))
        else:
            ans.append((i,stages.count(i)/person_num))
        person_num-=stages.count(i)
    ans.sort(key=lambda x: (-x[1], x[0]))
    return [i[0] for i in ans]

# 나누기 연산이 있을 때는 항상 zero divison error 확인하기!