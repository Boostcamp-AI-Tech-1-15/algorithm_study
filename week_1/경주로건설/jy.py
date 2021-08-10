def solution(board):
    ans = 0
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오, 아래, 왼, 위
    n = len(board)
    costs = [[[float('inf')]*4 for _ in range(n)] for _ in range(n)]
    for i in range(4):
        costs[0][0][i] = 0
    stack = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3)]
    while stack: 
        x, y, k = stack.pop()
        cost = costs[x][y][k]
        for i in range(4):
            a, b = x+d[i][0], y+d[i][1]
            if 0<=a<n and 0<=b<n and board[a][b]==0:
                if i==k:
                    n_cost = cost + 100
                else:
                    n_cost = cost + 100 + 500
                if n_cost<costs[a][b][i]:
                    costs[a][b][i] = n_cost
                    stack.append((a, b, i))
    ans = min(costs[n-1][n-1])
    return ans