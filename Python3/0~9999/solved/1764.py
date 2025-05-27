def a(b, c, d, e):
    d_set = set(d)
    e_set = set(e)
    
    result = sorted(d_set & e_set)
    
    return len(result), result

b, c = map(int, input().split())
d = [input().strip() for _ in range(b)]
e = [input().strip() for _ in range(c)]

count, names = a(b, c, d, e)
print(count)
print("\n".join(names))
