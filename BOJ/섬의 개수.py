from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if a[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    a = []
    visited = [[0] * w for _ in range(h)]
    dx = [-1, 1, 0, 0, 1, -1, -1, 1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    for i in range(h):
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and a[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

# BFS문제 위치설정을 대각선도 포함시켜준다.