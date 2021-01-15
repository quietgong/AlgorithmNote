###############################################
# 초기화
# m만큼의 1차원 배열 초기화
arr = [0] * m 

# n*m 크기의 2차원 배열 초기화
arr = [[0] * m for _ in range(n)] 

# 특정한 값의 원소 모두 제거하기
arr = [1,2,3,4,5,5,5]
remove_set = {3,5} # arr의 원소 3, 5를 제거하고자 한다.
arr = [i for i in arr if i not in remove_set]
print(arr)


###############################################
# 입출력

# input ex) 5
n = int(input())

# input ex) 3 5 7
n,m,k = map(int, input().split())

# input ex) 50 30 40 50 20
arr = list(map(int, input().split()))

# 2차원 배열 형태 입력
arr = [[int(x) for x in input().split()] for y in range(10)] 

# n*m 행렬 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print('')

# n만큼 줄바꿈으로 구별하여 빠른 입력 
# input ex)
# 1
# 2
# 3

import sys

n = int(input())
i=0
data = []

for i in range(n):
  data.append(sys.stdin.readline().rstrip())

print(data)
###############################################
# 순열, 조합

###############################################
# 이진탐색
from bisect import bisect_left, bisect_right

def CountByRange(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(CountByRange(a,4,4)) # 원소가 4인 데이터의 개수 출력

print(CountByRange(a,-1,3)) # 원소의 값이 [-1,3]인 데이터의 개수 출력
###############################################
# collections
from collections import deque

data = deque([1,2,3,4])
data.append() #맨 뒤에 원소 추가
data.appendleft() #맨 앞에 원소 추가
data.pop() #맨 뒤에 원소 삭제
data.popleft() #맨 앞에 원소 삭제