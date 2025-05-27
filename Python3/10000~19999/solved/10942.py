import sys
input = sys.stdin.readline
print = sys.stdout.write

def s():
    N = int(input())
    n = list(map(int, input().split()))
    M = int(input())
    
    dp = [[0] * N for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = 1
    
    for i in range(N-1):
        if n[i] == n[i+1]:
            dp[i][i+1] = 1
    
    for length in range(3, N+1):
        for i in range(N-length+1):
            j = i + length - 1
            if n[i] == n[j] and dp[i+1][j-1]:
                dp[i][j] = 1
    
    for _ in range(M):
        S, E = map(int, input().split())
        print(f"{dp[S-1][E-1]}\n")

s()