MOD = 10**8 + 7
K_MAX = 10

def m(a, b):
    s1, s2, s3 = len(a), len(b), len(b[0])
    c = [[0] * s3 for _ in range(s1)]
    
    for i in range(s1):
        for j in range(s3):
            for k in range(s2):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= MOD
    
    return c

def e(x):
    a = [[0] * (k + 1) for _ in range(k + 1)]
    ret = [[1 if i == j else 0 for j in range(k + 1)] for i in range(k + 1)]
    
    a[0][0] = a[0][k] = 1
    for i in range(1, k + 1):
        a[i][i - 1] = 1
    
    while x:
        if x % 2:
            ret = m(ret, a)
        a = m(a, a)
        x //= 2
    return ret

def e1(x):
    ret, a = 1, 2
    while x:
        if x % 2:
            ret *= a
            ret %= MOD
        a *= a
        a %= MOD
        x //= 2
    return ret

t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    
    if k == 0:
        print(e1(n) % MOD)
        continue
    
    f = [0] * (K_MAX + 1)
    f[0] = 1
    for i in range(1, k + 1):
        f[i] = f[i - 1]
        if i - k - 1 >= 0:
            f[i] += f[i - k - 1]
    
    if n <= k:
        print(f[n] % MOD)
        continue
    
    res = e(n - k)
    
    x = [[f[k - i]] for i in range(k + 1)]
    
    ans = m(res, x)
    print(ans[0][0])