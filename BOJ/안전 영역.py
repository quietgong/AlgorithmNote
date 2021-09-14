from collections import deque

size = int(input())
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
max_num=[]
ans=[]
for i in range(size):
    board.append(list(map(int, input().split())))
    max_num.append(max(board[i]))
max_height = max(max_num)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y]=1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and board[nx][ny]>height and visit[nx][ny]==0:
                visit[nx][ny] = 1
                q.append((nx, ny))

for height in range(max_height+1):
    cnt = 0
    visit = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if visit[i][j] == 0 and board[i][j]>height:
                bfs(i, j)
                cnt += 1
    ans.append(cnt)

print(max(ans))

# 최대높이까지만 조건설정