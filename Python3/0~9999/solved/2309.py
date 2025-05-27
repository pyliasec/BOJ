h = []
for _ in range(9):
    h.append(int(input()))

s = sum(h)

for i in range(9):
    for j in range(i + 1, 9):
        if s - (h[i] + h[j]) == 100:
            x, y = h[i], h[j]
            break
    if s - (h[i] + h[j]) == 100:
        break

r = [k for k in h if k != x and k != y]

r.sort()
for k in r:
    print(k)