res=[]
def dfs(graph, v, visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            visited[i]=True
            res.append(i)
            dfs(graph, i, visited)

n = int(input())
m = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a,b=map(int, input().split())
    matrix[a][b]=1
    matrix[b][a]=1

for i in range(1, len(matrix)):
    for j in range(n+1):
        if matrix[i][j]!=0:
            graph[i].append(j)
dfs(graph,1,visited)
print(len(res))

# 탐색