n = int(input())
condos = [tuple(map(int, input().split())) for _ in range(n)]

condos.sort(key=lambda x: (x[0], x[1]))

min_cost = float('inf')
count = 0

for d, c in condos:
    if c < min_cost:
        count += 1
        min_cost = c

print(count)
