def a(N, M, K):
    if K >= 3:
        s = K - 3
        p = (M - 1 + s) % N + 1
    else:
        s = 3 - K
        p = (M - 1 - s + N) % N + 1

    return p

N, M, K = map(int, input().split())

r = a(N, M, K)
print(r)