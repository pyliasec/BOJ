def min_coin(n):
    INF = float('inf')
    dp = [INF] * (n + 1)
    
    dp[0] = 0
    
    coins = [1, 2, 5, 7]
    
    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != INF:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[n] if dp[n] != INF else -1

n = int(input())
print(min_coin(n))