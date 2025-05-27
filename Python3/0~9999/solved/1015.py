def a(c, b):
    indexed_b = [(value, idx) for idx, value in enumerate(b)]
    indexed_b.sort()
    
    p = [0] * c
    for rank, (_, idx) in enumerate(indexed_b):
        p[idx] = rank
    
    return p

c = int(input().strip())
b = list(map(int, input().strip().split()))

result = a(c, b)
print(" ".join(map(str, result)))
