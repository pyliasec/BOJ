import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    chk = [[False] * 301 for _ in range(301)]
    dp = [[0] * 301 for _ in range(301)]

    for _ in range(N):
        C, R = map(int, input().split())
        chk[C - R + 100][C + R + 100] = True

    for gap in range(300):
        for start in range(1, 301 - gap):
            end = start + gap
            for mid in range(start + 1, end):
                dp[start][end] = max(dp[start][end], dp[start][mid] + dp[mid][end] + chk[start][end])

    print(N - dp[1][300])

solve()