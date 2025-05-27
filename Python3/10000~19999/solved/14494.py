MOD = 1000000007

def c(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]) % MOD
    
    return dp[n][m]

n, m = map(int, input().split())

print(c(n, m))