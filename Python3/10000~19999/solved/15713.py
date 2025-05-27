from heapq import heappush, heappop

n, k = map(int, input().split())

a = []
for _ in range(n):
    a.append(tuple(map(int, input().split())))
a.sort()

s = 0
while s < n and a[s][0] == 0:
    s += 1

if s == 0:
    print("Ducks can't fly")
else:
    q = [(0, s - 1)]
    v = set()

    while q:
        d, i = heappop(q)

        if i == 123456:
            print(d)
            exit()

        if i in v:
            continue
        v.add(i)

        g = a[i][0] + a[i][1]
        if g >= k:
            heappush(q, (d + k - a[i][0], 123456))
            continue

        l, r = i, n - 1
        while l <= r:
            m = (l + r) // 2
            if g >= a[m][0]:
                l = m + 1
            else:
                r = m - 1

        if r > i and r not in v:
            heappush(q, (d + a[i][1] + g - a[r][0], r))

        if i > 0 and i - 1 not in v:
            heappush(q, (d + a[i][0] - a[i-1][0], i - 1))

    print("Ducks can't fly")