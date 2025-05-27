def indentation(s):
    MOD = 1_000_000_007
    n = len(s)

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        char = s[i - 1]

        if char == 'f':
            for j in range(i, 0, -1):
                dp[j] = dp[j - 1]
            dp[0] = 0
        else:
            for j in range(i - 1, -1, -1):
                dp[j] = (dp[j] + dp[j + 1]) % MOD


    return dp[0]

s = input().strip()
print(indentation(s))