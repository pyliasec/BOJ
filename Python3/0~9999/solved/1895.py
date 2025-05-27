R, C = map(int, input().split())

a = []
for _ in range(R):
    b = list(map(int, input().split()))
    a.append(b)

T = int(input())

c = []
for i in range(1, R-1):
    d = []
    for j in range(1, C-1):
        e = [
            a[i-1][j-1], a[i-1][j], a[i-1][j+1],
            a[i][j-1], a[i][j], a[i][j+1],
            a[i+1][j-1], a[i+1][j], a[i+1][j+1],
        ]
        f = sorted(e)[4]
        d.append(f)
    c.append(d)

g = sum(1 for d in c for h in d if h >= T)

print(g)