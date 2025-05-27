def p(a, b, c):
    d = 1
    a %= c
    while b:
        if b & 1:
            d = d * a % c
        a = a * a % c
        b >>= 1
    return d

n = int(input())
*a, = map(int, input().split())
m = int(input())

if n < 2:
    print(p(a[1], a[0], m) if n else a[0] % m)
else:
    print(p(a[2], p(a[1], a[0], m-1) + m-1, m))