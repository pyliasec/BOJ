n, k = map(int, input().split())
pl = list(range(1, n + 1))

de = []
num = 0

for _ in range(n):
    num = (num + k - 1) % len(pl)
    de.append(str(pl.pop(num)))

result = "<" + ', '.join(de) + ">"
print(result)