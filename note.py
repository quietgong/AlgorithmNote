# 정수로 받은뒤, 배열로 바꾸고, 각 배열의 원소를 정수로 취급하기
n=list(str(n))
n=list(map(int, n))

###############################################

# 순서유지하면서 중복제거
arr = [0,1,1,3,3,5,5,5,7]
list(dict.fromkeys(arr)) # [0,1,3,5,7]

###############################################
# n진수 변환
def convert(n,q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q) # divmod 함수, n은 n을 q로 나눈 몫, mod는 n을 q로 나눈 나머지
        rev_base += str(mod)
    return rev_base[::-1]

###############################################
# array[::] 용법
arr = [0,1,2,3,4,5,6,7,8,9]
arr[::2] # 처음부터 끝까지 두 칸 간격으로 [0,2,4,6,8]
arr[1::2] # index 1 부터 끝까지 두 칸 간격으로 [1,3,5,7,9] 
arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로) [9,8,7,6,5,4,3,2,1,0]
arr[::-2] # 처음부터 끝까지 -2칸 간격으로 ( == 역순, 두 칸 간격으로) [9,7,5,3,1]
arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 ( == 역순으로) [3,2,1,0] 
arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로 [1,3,5]

###############################################
# 경우의 수 리스트 형태로 반환하기
import itertools

data = [1, 2, 3]

for x in itertools.permutations(data, 2):
    print(list(x))

###############################################
# 특정한 값의 원소 모두 제거하기
arr = [1,2,3,4,5,5,5]
remove_set = {3,5} # arr의 원소 3, 5를 제거하고자 한다.
arr = [i for i in arr if i not in remove_set]
print(arr)

###############################################
# 순열, 조합
from itertools import permutations

arr = [3, 5, 7]
print(list(permutations(arr, 2)))  # arr 에서 중복없이, 순서 상관없이 2개를 뽑는 경우의 수

from itertools import combinations

arr = [3, 5, 7]
print(list(combinations(arr, 2)))  # arr 에서 중복없이, 순서에 따라 2개를 뽑는 경우의 수

from itertools import product

arr = [3, 5, 7]
print(list(product(arr, repeat=2)))  # arr 에서 중복허용, 순서 상관없이 2개를 뽑는 경우의 수

from itertools import combinations_with_replacement

arr = [3, 5, 7]
print(list(combinations_with_replacement(arr, 2)))  # arr 에서 중복허용, 순서 상관에 따라 2개를 뽑는 경우의 수

###############################################
#파이썬에서 데이터 타입(str, int, list)간의 변환

# 1. int 형변환
num = 120
num = str(num)  # num = str type
num = list(str(num))  # num = list type

# 2. list(int 원소) 형변환
arr = [1, 2, 3]
for i in range(len(arr)):
    arr[i] = str(arr[i])
arr = ''.join(arr)  # arr = str type
arr = int(arr)  # arr = int type

# 3. list(str 원소) 형변환
arr = ["1", "2", "3"]
arr = ''.join(arr)  # arr = str type
arr = int(arr)  # arr = int type

# 4. str 형변환
string = "50"
string = int(string)  # string = int type
string = list(string)  # string = list type

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

# deque 활용
from collections import deque

data = deque([1,2,3,4])
data.append() #맨 뒤에 원소 추가
data.appendleft() #맨 앞에 원소 추가
data.pop() #맨 뒤에 원소 삭제
data.popleft() #맨 앞에 원소 삭제
###############################################
# 2차원 리스트(행렬)을 90도 회전시키는 함수 #

def rotate_a_matrix_90_degree(a):
  row_length = len(a) # 행렬의 행 길이
  column_length = len(a[0]) # 행렬의 열 길이
  
  res = [[0] * row_length for _ in range(column_length)] # 2차원 행렬 초기화

  for r in range(row_length):
    for c in range(column_length):
      res[c][row_length - 1 - r] = a[r][c]
  
  return res

# 2차원 리스트(행렬)을 180도 회전시키는 함수 #

def rotate_a_matrix_180_degree(a):
  row_length = len(a) # 행렬의 행 길이
  column_length = len(a[0]) # 행렬의 열 길이
  
  res = [[0] * column_length for _ in range(row_length)] # 2차원 행렬 초기화

  for r in range(row_length):
    for c in range(column_length):
      res[row_length - 1 - r][column_length - 1 - c] = a[r][c]
  
  return res

# 2차원 리스트(행렬)을 270도 회전시키는 함수 #

def rotate_a_matrix_270_degree(a):
  row_length = len(a) # 행렬의 행 길이
  column_length = len(a[0]) # 행렬의 열 길이
  
  res = [[0] * row_length for _ in range(column_length)] # 2차원 행렬 초기화

  for r in range(row_length):
    for c in range(column_length):
      res[column_length -1 - c][r] = a[r][c]
  
  return res

a = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]

print(rotate_a_matrix_90_degree(a))
print(rotate_a_matrix_180_degree(a))
print(rotate_a_matrix_270_degree(a))
###############################################
# 아스키코드
chr(97) = 'a'
ord('a') = 97