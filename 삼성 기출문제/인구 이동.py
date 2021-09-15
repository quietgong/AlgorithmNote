from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp = []
    temp.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and status[nx][ny] == 0:
                if L <= abs(board[nx][ny] - board[x][y]) <= R:
                    status[nx][ny] = 1
                    q.append((nx, ny))
                    temp.append([nx, ny])
    return temp


N, L, R = map(int, input().split())
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    board.append(list(map(int, input().split())))

ans = 0
while True:
    status = [[0] * N for _ in range(N)]
    isTrue = False
    for i in range(N):
        for j in range(N):
            if status[i][j] == 0:
                status[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:  # 연합이 있을때 (연합구역이 2이상일때)
                    isTrue = True
                    total_num = 0
                    for x, y in temp:
                        total_num += board[x][y]
                    new_population = total_num // len(temp)
                    for x, y in temp:
                        board[x][y] = new_population
    if not isTrue:
        break
    ans += 1
    print(ans)

# 포인트
# BFS의 queue에 삽입되는 좌표의 의미를 더 이해하기
# arr=[[2, 2], [3, 2], [3, 1], [3, 3]]
# for x,y in arr:
#     print(x,y)
# 2 2
# 3 2
# 3 1
# 3 3
