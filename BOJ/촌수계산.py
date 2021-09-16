from collections import deque

n = int(input())
s, f = map(int, input().split())
edge = int(input())
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
distance = [0] * (n + 1)
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque([start])
    visit[start] = True
    while q:
        print(q)
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = True
                print(f"v={v},i={i}")
                q.append(i)
                distance[i] = distance[v] + 1 # 노드 i(노드 v와 연결된)의 거리는 노드 v 의 거리에 1을 더한 값이다.
    if distance[f] == 0:
        return -1
    else:
        return distance[f]


print(bfs(s))
