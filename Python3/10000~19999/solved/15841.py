def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

while True:
    h = int(input())
    if h == -1:
        break
    c = f(h)
    print(f"Hour {h}: {c} cow(s) affected")