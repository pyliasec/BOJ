def solve():
    n = int(input())
    
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    
    a[0], b[0], c[0] = 0, 0, 1
    
    for i in range(1, n + 1):
        a[i] = a[i - 1] - c[i - 1]
        b[i] = b[i - 1] + c[i - 1]
        c[i] = 2 * a[i - 1] - 2 * b[i - 1] + c[i - 1]
    
    print(a[n] + b[n] + c[n])

solve()