from itertools import combinations

def solution(numbers):
    arr=[]
    ans=[]
    for x in combinations(numbers,2):
        arr.append(list(x))
    for i in range(len(arr)):
        ans.append(arr[i][0]+arr[i][1])
    ans = list(set(ans))
    ans.sort()
    return ans

# 경우의 수를 리스트로 반환하기 (맨날 까먹음)