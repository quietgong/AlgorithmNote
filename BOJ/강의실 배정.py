import heapq
import sys
n = int(input())
a = [[0] * 2 for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().split()))
a.sort()
q=[]
heapq.heappush(q, a[0][1])
for i in range(1, len(a)):
    if a[i][0] < q[0]:
        heapq.heappush(q, a[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, a[i][1])

print(len(q))

# 우선순위 큐를 만들어서 리스트의 다음 원소의 시작 시간이 이전 원소의 끝나는 시간보다 작으면 push, 그렇지 않으면 기존에 있던
# 가장 작은 값을 pop해준 뒤 새로운 원소를 push 해주고, 큐의 길이를 출력하면 된다.