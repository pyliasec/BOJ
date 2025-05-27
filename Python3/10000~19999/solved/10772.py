def c(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] += dp[i - 1][j - 1]
            
            if i > j:
                dp[i][j] += dp[i - j][j]
    
    return dp[n][k]

n = int(input())
k = int(input())

result = c(n, k)
print(result)