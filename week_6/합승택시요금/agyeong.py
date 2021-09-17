from collections import deque

def solution(n, s, a, b, fares):
    
    # 출발과 도착 지점 비용
    _fares = fares
    fares = [[] for _ in range(n+1)]
    for c, d, f in _fares:
        fares[c].append((d, f))
        fares[d].append((c, f))
    
    # 특정 지점으로 갈 때 가장 멀리 돌아가도 100000 * n 보다 클 수 없음. 
    # 더 정확하게 말하자면 최대 거리가 100000 * (n-1) 이 최대.
    max_dist = 100000 * n        # 100000 * (n-1) + 1 이라고 해도 됨.
    
    # s에서 모든 지점간의 거리 
    from_s = [max_dist] * (n+1)  # 지점은 1부터 n까지 
    q = deque([(s, 0)])          # 시작 지점, 비용 
    from_s[s] = 0                # 시작 지점의 비용은 0
    
    while q:
        c_pos, c_dist = q.popleft()                 # 현재 지점(위치), 비용 
        if from_s[c_pos] < c_dist:                  
            continue
        
        for n_pos, n_dist in fares[c_pos]:          # 현재 지점과 연결된 지점 방문 
            if from_s[n_pos] >= c_dist + n_dist:    # 새로운 경로의 비용이 더 작다면
                from_s[n_pos] = c_dist + n_dist     # 업데이트 
                q.append((n_pos, c_dist + n_dist))  
    
    # 모든 지점에서 a로의 거리 
    to_a = [max_dist] * (n+1)
    q = deque([(a, 0)])
    to_a[a] = 0
    
    while q:
        c_pos, c_dist = q.popleft()
        if to_a[c_pos] < c_dist:
            continue
        
        for n_pos, n_dist in fares[c_pos]:
            if to_a[n_pos] >= c_dist + n_dist:
                to_a[n_pos] = c_dist + n_dist
                q.append((n_pos, c_dist + n_dist))
                
    # 모든 지점에서 b로의 거리         
    to_b = [max_dist] * (n+1)
    q = deque([(b, 0)])
    to_b[b] = 0
    
    while q:
        c_pos, c_dist = q.popleft()
        if to_b[c_pos] < c_dist:
            continue
        
        for n_pos, n_dist in fares[c_pos]:
            if to_b[n_pos] >= c_dist + n_dist:
                to_b[n_pos] = c_dist + n_dist
                q.append((n_pos, c_dist + n_dist))
    
    # 합승하는 지점까지의 최단 비용 + 합승이 끝난 시점에서 a, b 각각 집에 가는 최단 비용 중 최소값 
    return min([a + b + c for a, b, c in zip(from_s, to_a, to_b)]) 