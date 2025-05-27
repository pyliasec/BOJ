def b(n, sizes):
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if sizes[i] > sizes[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

n = int(input())
sizes = list(map(int, input().split()))

result = b(n, sizes)
print(result)