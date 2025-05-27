def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    f1 = [0] * (n + 1)
    f1[0] = 0
    f1[1] = 1
    
    for i in range(2, n + 1):
        f1[i] = f1[i - 1] + f1[i - 2]
    
    return f1[n]

n = int(input())
print(f(n))
