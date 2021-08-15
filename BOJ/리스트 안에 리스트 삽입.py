import sys

n = int(sys.stdin.readline())

li = []  # 2차원리스트
for _ in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    li.append(xy)

li.sort()
for i in li:
    print(i[0], i[1])