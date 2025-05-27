def f(n):
    fib = [(1, 0), (0, 1)] + [(0, 0)] * 39
    
    for i in range(2, n + 1):
        fib[i] = (fib[i-1][0] + fib[i-2][0], fib[i-1][1] + fib[i-2][1])

    return fib[n]

T = int(input())

for _ in range(T):
    N = int(input())
    z, o = f(N)
    print(z, o)