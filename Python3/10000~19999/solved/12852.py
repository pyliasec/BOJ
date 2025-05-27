def o(N):
    dp = [0] * (N + 1)
    p = [0] * (N + 1)
    
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        p[i] = i - 1
        
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            p[i] = i // 2
        
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            p[i] = i // 3
    
    result = [N]
    while N != 1:
        N = p[N]
        result.append(N)
    
    return dp[-1], result

N = int(input())

m, p = o(N)

print(m)
print(*p)