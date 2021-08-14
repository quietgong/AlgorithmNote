from collections import deque
n = int(input())
deque = deque()
for i in range(1, n+1):
    deque.append(i)

for i in range(n):
    if len(deque) == 1:
        break
    deque.popleft()
    deque.append(deque[0])
    deque.popleft()

print(deque[0])