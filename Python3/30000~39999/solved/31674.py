MOD = 10**9 + 7

def a(N, b):
    b.sort(reverse=True)
    s = 0
    for i in b:
        s = (s + s + i) % MOD
    return s

N = int(input())
b = list(map(int, input().split()))

print(a(N, b))