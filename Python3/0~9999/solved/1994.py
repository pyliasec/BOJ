def f(a):
    n = len(a)
    if n <= 2: return n
    a.sort()
    d = [{} for _ in range(n)]
    m = 2
    for i in range(1, n):
        for j in range(i):
            df = a[i] - a[j]
            d[i][df] = d[j].get(df, 1) + 1
            m = max(m, d[i][df])
    return m

n = int(input())
a = [int(input()) for _ in range(n)]
print(f(a))