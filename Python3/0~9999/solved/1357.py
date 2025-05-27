x, y = map(int, input().split())

r = int(str(x)[::-1]) + int(str(y)[::-1])
r = int(str(r)[::-1])

print(r)