s = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

n1 = input().strip()
n2 = input().strip()

n = []
for a, b in zip(n1, n2):
    n.append(s[ord(a) - ord('A')])
    n.append(s[ord(b) - ord('A')])

while len(n) > 2:
    nn = []
    for i in range(len(n) - 1):
        nn.append((n[i] + n[i+1]) % 10)
    n = nn

print(f"{n[0]}{n[1]}")