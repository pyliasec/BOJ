def y(n, k):
    if k == 1:
        return n

    ans = 0
    nn = 1

    while True:
        x = (nn - ans - 1) // (k - 1) + 1
        if nn + x > n:
            ans += (n - nn) * k
            break
        ans = (ans + k * x) % (nn + x)
        nn += x

    return ans + 1

n, k = map(int, input().split())
print(y(n, k))