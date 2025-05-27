def c(grid):
    for row in grid:
        if 'w' in row:
            return 'chunbae'
        elif 'b' in row:
            return 'nabi'
        elif 'g' in row:
            return 'yeongcheol'

grid = []
for _ in range(15):
    row = input().split()
    grid.append(row)

cat = c(grid)
print(cat)