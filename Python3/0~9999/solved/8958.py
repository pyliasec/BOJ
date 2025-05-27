def c(q):
    s = 0
    a = 0
    for result in q:
        if result == 'O':
            a += 1
            s += a
        else:
            a = 0
    return s

n = int(input())

for _ in range(n):
    q = input().strip()
    print(c(q))