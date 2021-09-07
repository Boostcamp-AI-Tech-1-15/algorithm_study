def solution(n, s, a, b, fares):
    ans = float('inf')
    costs = [[float('inf')]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        costs[i][i] = 0
    
    for c, d, fare in fares:
        costs[c][d] = fare
        costs[d][c] = fare
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    for i in range(1, n+1):
        
        ans = min(ans, costs[s][i]+costs[i][a]+costs[i][b])
 
    return ans