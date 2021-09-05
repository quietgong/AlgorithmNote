import sys
from collections import deque

t = int(input())
for _ in range(t):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    is_error = False
    q = deque(arr)
    r_num=0
    if n==0:
        q = []

    for i in command:
        if i == 'R':
            r_num+=1
        elif i == 'D':
            if len(q) == 0:
                print("error")
                is_error = True
                break
            else:
                if r_num%2==0:
                    q.popleft()
                else:
                    q.pop()

    if not is_error:
        if r_num%2==0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")

# 뒤집는 개수가 홀수인 것과 짝수인것을 나누어서 풀면됨.
# arr = sys.stdin.readline().rstrip()[1:-1].split(",")
# print("[" + ",".join(q) + "]")