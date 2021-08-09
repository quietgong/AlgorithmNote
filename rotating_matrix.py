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