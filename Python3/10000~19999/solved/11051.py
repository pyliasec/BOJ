def fac(n):
    ans = 1
    for i in range(2, n+1):
        ans = (ans * i) % 10007
    return ans

def get_comb(N, K):
    return (fac(N) * pow(fac(K) * fac(N-K) % 10007, 10005, 10007)) % 10007

N, K = map(int, input().split())
print(get_comb(N, K))