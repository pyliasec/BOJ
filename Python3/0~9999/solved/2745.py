n, b = input().split()
b = int(b)

r = 0
for i, d in enumerate(reversed(n)):
    if '0' <= d <= '9':
        v = ord(d) - ord('0')
    else:
        v = ord(d) - ord('A') + 10
    r += v * (b ** i)

print(r)