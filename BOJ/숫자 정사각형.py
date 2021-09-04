n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input())))
size = 1
max_size = min(n, m)
for t in range(1, max_size):
    for i in range(n):
        for j in range(m):
            if i + t >= n or j + t >= m or i >= n or j >= m:
                continue
            if a[i][j] == a[i + t][j] == a[i][j + t] == a[i + t][j + t]:
                size = (t + 1) ** 2
print(size)
# 구현, 브루트포스 (index 범위내로 탐색조건 설정)