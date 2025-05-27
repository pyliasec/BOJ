def a(N, A):
    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(N):
        if dp[i] == float('inf'):
            continue
        for j in range(1, A[i] + 1):
            if i + j < N:
                dp[i + j] = min(dp[i + j], dp[i] + 1)

    return dp[N-1] if dp[N-1] != float('inf') else -1

N = int(input())
A = list(map(int, input().split()))

print(a(N, A))