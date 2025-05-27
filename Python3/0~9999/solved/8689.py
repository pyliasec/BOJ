def s(n, v):
    dp = [-float('inf')] * (n + 1)
    dp[1] = v[0]

    for i in range(1, n + 1):
        for j in range(1, 7):
            if i + j <= n:
                dp[i + j] = max(dp[i + j], dp[i] + v[i + j - 1])

    return dp[n]

n = int(input())
v = list(map(int, input().split()))

print(s(n, v))