import sys
sys.setrecursionlimit(10**5)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)

# dfs or bfs, 재귀한계 설정