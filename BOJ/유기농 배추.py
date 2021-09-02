import sys
sys.setrecursionlimit(10**5)
def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if matrix[x][y] == 1:
        matrix[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


t = int(input())
for _ in range(t):
    res = 0
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                res += 1
    print(res)

# DFS 문제, 재귀 limit 설정