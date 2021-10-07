n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 맨 앞자리
            arr[i][j] += arr[i - 1][j]
        elif j == i: # 맨 끝자리
            arr[i][j] += arr[i - 1][j - 1]
        else: # 맨 앞자리와 맨 끝자리 사이
            arr[i][j] = max(arr[i][j] + arr[i - 1][j], arr[i][j] + arr[i - 1][j - 1])
print(max(arr[n - 1]))

# 더해가면서 저장하기 (DP)
# 프로그래머스 정수 삼각형과 동일