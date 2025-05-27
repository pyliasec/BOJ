import sys
input = sys.stdin.readline
n, k, x = map(int, input().split())
a = [int(input().split()[0]) for _ in range(n)]
dp = [1] + [0] * k
for v in a:
    for j in range(k - 1, -1 ,-1):
        dp[j + 1] |= dp[j] << v
t = k * x
d = dp[k]
print(max(s * (t - s) for s in range(d.bit_length()) if d >> s & 1))