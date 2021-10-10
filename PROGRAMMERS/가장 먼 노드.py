import heapq

INF = int(1e9)

def solution(n, edge):
    graph = [[] for i in range(n + 1)]
    for i in edge:
        a,b = i[0],i[1]
        graph[a].append((b, 1))
        graph[b].append((a,1))
    distance = [INF] * (n + 1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijkstra(1)
    for i in range(len(distance)):
        if distance[i]==INF:
            distance[i]=-1
    return distance.count(max(distance))

# 다익스트라 알고리즘을 활용해 distance 리스트에 INF값을 제외한 가장 큰값의 개수를 리턴