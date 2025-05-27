from collections import deque

a, b, c, d = map(int, input().split())
e = [False] * (a + 1)

for _ in range(b):
    f, g = map(int, input().split())
    for h in range(f, g + 1):
        e[h] = True

i = deque([(0, 0)])
j = [-1] * (a + 1)
j[0] = 0

while i:
    k, l = i.popleft()
    
    if k == a:
        print(l)
        exit()
    
    for m in [c, d]:
        n = k + m
        if n <= a and not e[n] and j[n] == -1:
            j[n] = l + 1
            i.append((n, l + 1))

print(-1)