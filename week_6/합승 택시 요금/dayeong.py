import heapq

INF = int(1e9)

def dijkstra(graph, start, n):
    q = []
    distance = [INF] * (n + 1)
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
    return distance

def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n + 1)]
    
    for start, dst, cost in fares:
        # 양방향
        graph[start].append((dst, cost))
        graph[dst].append((start, cost))
    for i in range(1, n + 1):
        dist = dijkstra(graph, i, n)
        answer = min(answer, dist[s] + dist[a] + dist[b])
    return answer