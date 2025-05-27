def c(N, num):
    dp = [[[0 for _ in range(21)] for _ in range(N)] for _ in range(2)]
    
    dp[1][0][num[0]] = 1

    for i in range(1, N-1):
        for j in range(21):
            if dp[1][i-1][j] > 0:
# 덧셈
                if j + num[i] <= 20:
                    dp[1][i][j + num[i]] += dp[1][i-1][j]
# 뺄셈
                if j - num[i] >= 0:
                    dp[0][i][j - num[i]] += dp[1][i-1][j]
            
            if dp[0][i-1][j] > 0:
# 덧셈
                if j + num[i] <= 20:
                    dp[1][i][j + num[i]] += dp[0][i-1][j]
# 뺄셈
                if j - num[i] >= 0:
                    dp[0][i][j - num[i]] += dp[0][i-1][j]
    
    return dp[0][N-2][num[-1]] + dp[1][N-2][num[-1]]

N = int(input())
numbers = list(map(int, input().split()))

result = c(N, numbers)
print(result)