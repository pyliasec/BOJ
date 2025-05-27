MOD = 20150523

def p():
    N = 10**5 + 1
    DP = [[0] * N for _ in range(3)]
    DP[0][0] = 1
    
    for i in range(1, N):
        for r in range(3):
            for r0 in range(3):
                DP[r][i] += DP[r0][i-1] * (3 - 2 * int(r == r0))
            DP[r][i] %= MOD
    return DP

def solve(X):
    X = list(map(int, str(X)))
    L = len(X)
    
    for l in range(L):
        if X[l] and X[l] % 3 == 0:
            X[l] -= 1
            X[l+1:] = [8] * (L - l - 1)
    
    cnt = R = 0
    for l in range(L):
        x = int(X[l])
        for i in range(x):
            if i and i % 3 == 0:
                continue
            for r in range(3):
                if (R + i + r) % 3 != 0:
                    cnt += DP[r][L - l - 1]
        R += x
        R %= 3
        cnt %= MOD
    
    return cnt + int(R != 0)

DP = p()

A, B = map(int, input().split())
A -= 1

result = (B - A - solve(B) + solve(A)) % MOD
print(result)