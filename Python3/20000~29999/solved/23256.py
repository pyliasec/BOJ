import sys

MOD = 10**9 + 7
d = [[0, 0] for _ in range(1_000_005)]

d[1][0] = 3
d[1][1] = 7

for i in range(2, 1_000_001):
    d[i][0] = (d[i - 1][0] * 2 + d[i - 1][1]) % MOD
    d[i][1] = (d[i - 1][0] * 4 + d[i - 1][1] * 3) % MOD

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(d[n][1])
