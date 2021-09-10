n, m = map(int, input().split())
floor = []
clean = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, direction = map(int, input().split())
clean[x][y] = 1
for i in range(n):
    floor.append(list(map(int, input().split())))


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if clean[nx][ny] == 0 and floor[nx][ny] == 0:
        clean[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if floor[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)
