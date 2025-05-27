N, M = map(int, input().split())
candies = [[0] * 301 for _ in range(301)]
dp = [[0] * 301 for _ in range(301)]

for _ in range(N):
    x, y = map(int, input().split())
    candies[x][y] = M

for i in range(301):
    for j in range(301):
        time = i + j
        candy = max(0, candies[i][j] - time) if candies[i][j] > 0 else 0
        
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        dp[i][j] += candy

print(dp[300][300])