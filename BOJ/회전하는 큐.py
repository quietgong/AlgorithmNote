from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

q = deque()
for i in range(n):
    q.append(i + 1)
i = 0
while a:
    if q[0] == a[0]:
        i += 1
        q.popleft()
        a.pop(0)
    else:
        if q.index(a[0]) <= len(q) // 2:
            q.rotate(-1)
        else:
            q.rotate(1)
        cnt += 1
print(cnt)

# deque의 rotate 활용 (찾고자 하는 수의 인덱스에 따라 왼쪽 회전 or 오른쪽 회전)