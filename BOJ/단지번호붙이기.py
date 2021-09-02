from collections import deque


def bfs(x, y, cnt):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = cnt


n = int(input())
matrix = []
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    matrix.append(list(map(int, input())))
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = 1
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and matrix[i][j] == 1:
            cnt += 1
            bfs(i, j, cnt)

for i in range(n):
    for j in range(n):
        if visited[i][j] != 0:
            ans.append(visited[i][j])

res = [0] * cnt
for i in range(len(ans)):
    res[ans[i] - 1] += 1
res.sort()
print(cnt)
for i in res:
    print(i)

# DFS/BFS