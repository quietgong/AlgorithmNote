from collections import deque

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().rstrip()))
visit = [[0] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    w = 0
    s = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visit[x][y] = 1
        if board[x][y] == 'o':  # 양
            s += 1
        elif board[x][y] == 'v':  # 늑대
            w += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == 0 and board[nx][ny] != '#':
                visit[nx][ny] = 1
                q.append((nx, ny))

    if w >= s:
        s = 0
    else:
        w = 0
    return w, s


wolf = 0
sheep = 0

for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and visit[i][j] == 0:
            w, s = bfs(i, j)
            wolf += w
            sheep += s
print(sheep, wolf)

# 함수와 외부코드의 변수명이 겹치지 않게!!