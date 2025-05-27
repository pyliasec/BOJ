def f1(n):
    global a
    if n == 1 or n == 2:
        a += 1
        return 1
    else:
        return f1(n - 1) + f1(n - 2)

def f2(n):
    global c
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        c += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())

a = 0
c = 0

f1(n)
f2(n)

print(a, c)