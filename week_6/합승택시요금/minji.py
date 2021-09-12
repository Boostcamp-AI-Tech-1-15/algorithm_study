import heapq


def dijkstra(graph, n, start):
    heap = []
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        cost, node = heapq.heappop(heap)

        # 기존에 있는 비용보다 많음
        if distance[node] < cost:
            continue

        for n, c in graph[node]:
            c += cost
            # 비용 갱신
            if c < distance[n]:
                distance[n] = c
                heapq.heappush(heap, [c, n])  # next

    return distance


def solution(n, s, a, b, fares):
    """
    n: 지점의 개수
    s: 출발 지점
    a: A의 도착 지점
    b: B의 도착 지점
    """
    # 그래프 생성
    graph = [[] for i in range(n + 1)]
    for fare in fares:
        point1, point2, cost = fare  # 지점 1, 지점 2, point1,2간 비용
        graph[point1].append((point2, cost))
        graph[point2].append((point1, cost))

    # dijkstra 결과 저장
    distance = [[]]
    for i in range(1, n + 1):
        distance.append(dijkstra(graph, n, i))

    # 결과 비교하여 최소비용 저장
    answer = float('inf')
    for stopover in range(1, n + 1):
        if stopover != s:
            # 합승 안하고 각자 타고감
            no_sharing = distance[s][a] + distance[s][b]
            # 합승 해서 stopover 까지 간 후 각자 타고감
            sharing = distance[s][stopover] + distance[stopover][a] + distance[stopover][b]
            # 최소비용 갱신
            answer = min(answer, no_sharing, sharing)
    return answer
