from collections import deque, defaultdict

def bfs(graph, start):
    q = deque([start])
    f = defaultdict(int)
    
    while q:
        curr = q.popleft()
        for next, fare in graph[curr]:
            if next != start and (f[next] > f[curr] + fare or f[next] == 0):
                f[next] = f[curr] + fare
                q.append(next)

    return f

def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = defaultdict(list)
    for i in range(len(fares)):
        c, d, f = fares[i]
        graph[c].append([d, f])
        graph[d].append([c, f])
    
    AB = bfs(graph, s)
    A = bfs(graph, a)
    B = bfs(graph, b)
        
    for i in range(1, n + 1):
        m = AB[i] + A[i] + B[i]
        if answer > m and m != 0:
            answer = m

    return answer
