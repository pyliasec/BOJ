def n15(N):
    MOD = 1000000007
    
    dp = [[0 for _ in range(15)] for _ in range(N+1)]
    
    dp[1][1] = 1
    dp[1][5] = 1
    
    for i in range(2, N+1):
        for j in range(15):
            dp[i][(j*10 + 1) % 15] = (dp[i][(j*10 + 1) % 15] + dp[i-1][j]) % MOD
            
            dp[i][(j*10 + 5) % 15] = (dp[i][(j*10 + 5) % 15] + dp[i-1][j]) % MOD
    
    return dp[N][0]

N = int(input())

result = n15(N)
print(result)