def S(s):
    return sum(int(c) for c in s if c.isdigit())

def C(s):
    return (len(s), S(s), s)

n = int(input())
b = [input() for _ in range(n)]

SS = sorted(b, key=C)

for a in SS:
    print(a)