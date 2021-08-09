import math

T = int(input())

for _ in range(T):
    res=0
    x, y = map(int, input().split())
    distance = y - x
    root_num = int(math.sqrt(distance)) + 1

    if distance == 0:
        print('0')
    else:
        if (root_num-1) * (root_num-1) - distance == 0:
            res = int(root_num + root_num - 3)
        elif root_num * root_num - distance < root_num:
            res = int(2*root_num - 1)
        else:
            res = int(2*root_num - 2)
        print(res)