from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
step = 0
while belt.count(0) < k:
    belt.rotate()
    robot.rotate()
    robot[-1] = 0

    if sum(robot) != 0:
        for i in range(n - 2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] > 0:  # i번째에 로봇이 있고 다음칸에 로봇이 없고 다음칸의 내구도가 0보다 크다면
                robot[i + 1] = 1  # 다음칸에 로봇을 이동
                robot[i] = 0  # 원래있던 칸의 로봇을 제거
                belt[i + 1] -= 1  # 다음 벨트의 내구도 감소
            robot[-1] = 0
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
    step += 1
print(step)

# 문제대로 구현하기
# for문의 인덱스를 감소시키는 테크닉
