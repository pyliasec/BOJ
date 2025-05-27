a = int(input())
b = input()
c = [float('inf')] * a
c[0] = 0

d = {'B': 0, 'O': 1, 'J': 2}

for i in range(a):
    if c[i] == float('inf'):
        continue
    for j in range(i+1, a):
        if d[b[j]] == (d[b[i]] + 1) % 3:
            c[j] = min(c[j], c[i] + (j-i)**2)

e = c[-1] if c[-1] != float('inf') else -1
print(e)