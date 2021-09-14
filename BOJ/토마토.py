from collections import deque

n, m = map(int, input().split())
board = []
tomato_position=deque()
for i in range(m):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j]==1:
            tomato_position.append((i,j))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while tomato_position:
        x,y=tomato_position.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny]==0:
                board[nx][ny]=board[x][y]+1
                tomato_position.append((nx,ny))


bfs()
ans=0
for i in board:
    for j in i:
        if j==0:
            print("-1")
            exit()
        ans = max(ans,max(i))
print(ans-1)

# 최단, 최소라는 조건이 붙을 때는 DFS가 아닌 "BFS"로 풀이
# 항상 방문여부를 확인하는 visit 변수가 필요한 것은 아니다.
# 미로 탐색과 동일