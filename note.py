# m만큼의 1차원 배열 초기화
arr = [0] * m 

# n*m 크기의 2차원 배열 초기화
arr = [[0] * m for _ in range(n)] 

# 특정한 값의 원소 모두 제거하기
arr = [1,2,3,4,5,5,5]
remove_set = {3,5} # arr의 원소 3, 5를 제거하고자 한다.
arr = [i for i in arr if i not in remove_set]
print(arr)

# 2차원 배열 형태 입력
arr = [[int(x) for x in input().split()] for y in range(10)] 

# n*m 행렬 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print('')