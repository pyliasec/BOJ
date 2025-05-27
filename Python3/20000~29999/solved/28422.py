def c(n):
    r = 0
    while n > 0:
        n &= (n - 1)
        r += 1
    return r

def m(a):
    n = len(a)
    d = [0] * (n + 1)

    if n >= 2:
        d[2] = c(a[0] ^ a[1])
        if n >= 3:
            d[3] = c(a[0] ^ a[1] ^ a[2])
        if n >= 4:
            d[4] = c(a[2] ^ a[3]) + d[2]

    for i in range(5, n + 1):
        x1 = a[i - 2] ^ a[i - 1]
        x2 = a[i - 3] ^ a[i - 2] ^ a[i - 1]
        d[i] = max(d[i - 2] + c(x1), d[i - 3] + c(x2))

    return d[n]

n = int(input())
a = list(map(int, input().split()))

print(m(a))