from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for i in range(m):
    line = list(map(int, input().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

for i in range(1, len(matrix)):
    for j in range(n+1):
        if matrix[i][j]!=0:
            graph[i].append(j)

dfs(graph, v, visited_dfs)
print("")
bfs(graph, v, visited_bfs)

# 간선->인접행렬->그래프