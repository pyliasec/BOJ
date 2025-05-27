def abs_val(k):
    return k if k >= 0 else -k

a, b = map(int, input().split())
d = abs_val(b - a)

if a == b:
    a = b = 1
else:
    while d % 2 == 0:
        d //= 2
    
    if a < b:
        a = 1
        b = 1 + d
    else:
        a = 1 + d
        b = 1

for _ in range(5):
    x, y = map(int, input().split())
    
    if (a <= b) != (x <= y):
        print("N")
    else:
        dd = abs_val(y - x)
        
        if d * dd == 0:
            print("Y" if d == dd else "N")
        else:
            print("Y" if dd % d == 0 else "N")