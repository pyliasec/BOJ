def cs(n, t):
    c = n + t
    L = c.count('L')
    O = c.count('O')
    V = c.count('V')
    E = c.count('E')
    
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

y = input().strip()
N = int(input().strip())
tn = [input().strip() for _ in range(N)]

bt = min(tn, key=lambda t: (-cs(y, t), t))

print(bt)