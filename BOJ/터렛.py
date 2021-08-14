import math

T = int(input())

for _ in range(T):

    p = list(map(int, input().split(' ')))
    d = math.sqrt(abs(p[0] - p[3]) ** 2 + abs(p[1] - p[4]) ** 2)

    r1 = p[2]
    r2 = p[5]

    if p[0] == p[3] and p[1] == p[4] and p[2] == p[5]:
        print("-1")
    elif abs(r1 - r2) < d < r2 + r1:
        print("2")
    elif r2 + r1 == d or abs(r1 - r2) == d:
        print("1")
    elif r2 + r1 < d or d < abs(r1 - r2) or d == 0.0:
        print("0")
