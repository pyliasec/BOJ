import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]

MOD = 1000000009

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[n - 1][m - 1] = 1
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        c = a[i][j]
        if c == 'X': continue
        if c == 'E':
            dp[i][j] = dp[i][j + 1]
        elif c == 'S':
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = (dp[i][j + 1]+dp[i + 1][j]) % MOD
r = 0
for i in range(n):
    for j in range(m):
        r = (r + dp[i][j]) % MOD
print(r)