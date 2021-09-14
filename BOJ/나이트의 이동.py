from collections import deque

t = int(input())
for _ in range(t):
    size = int(input())
    board = [[0] * size for _ in range(size)]

    x,y = map(int, input().split())
    f_x, f_y = map(int, input().split())
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        if x == f_x and y == f_y:
            break
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and board[nx][ny]==0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))
    print(board[f_x][f_y])

# 움직일 좌표 정확히
# 조건을 찾으면 break 문을 사용해 빠져나오기 (시간초과 방지)