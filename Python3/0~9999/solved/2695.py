def s(B, M):
    dp = [[0] * (M + 1) for _ in range(B + 1)]
    
    for j in range(M + 1):
        dp[1][j] = j
    
    for i in range(B + 1):
        dp[i][0] = 0
    
    for i in range(2, B + 1):
        for j in range(1, M + 1):
            dp[i][j] = float('inf')
            for k in range(1, j + 1):
                a = max(dp[i-1][k-1], dp[i][j-k]) + 1
                dp[i][j] = min(dp[i][j], a)
    
    return dp[B][M]

P = int(input())
for _ in range(P):
    B, M = map(int, input().split())
    result = s(B, M)
    print(result)