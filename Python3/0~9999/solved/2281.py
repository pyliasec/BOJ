import sys

def solve(n, m, l):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        ll = -1
        for j in range(i, 0, -1):
            if ll + 1 + l[j-1] > m:
                break
            ll += 1 + l[j-1]
            r = m - ll
            if j == 1:
                if i == n:
                    dp[i] = min(dp[i], dp[j-1])
                else:
                    dp[i] = min(dp[i], dp[j-1] + r * r)
            else:
                if i == n:
                    dp[i] = min(dp[i], dp[j-1])
                else:
                    dp[i] = min(dp[i], dp[j-1] + r * r)
    
    return dp[n]

input = sys.stdin.readline
n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]

print(solve(n, m, l))