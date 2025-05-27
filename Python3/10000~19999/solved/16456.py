MOD = 1000000009

def c(n):
    dp = [0] * 50000
    dp[0] = dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n):
        dp[i] = (dp[i - 1] + dp[i - 3]) % MOD
    
    return dp[n - 1]

n = int(input())

print(c(n))