a, d, k = map(int, input().split())

if (k - a) % d == 0:
    n = (k - a) // d + 1
    if n >= 1:
        print(n)
    else:
        print("X")
else:
    print("X")