def solution(n, wires):
    graph=[[] for _ in range(n+1)]
    ans=100
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    def dfs(graph, v, visited):
        visited[v]=True
        res.append(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    for wire in wires:
        visited=[False]*(n+1)
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        res=[]
        dfs(graph,wire[0],visited)
        a=len(res)
        res=[]
        dfs(graph,wire[1],visited)
        b=len(res)
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        ans=min(ans,abs(b-a))
    return ans

# 연결된 노드를 하나씩 잘라보면서 BFS 또는 DFS를 사용해 경로 개수 구하기