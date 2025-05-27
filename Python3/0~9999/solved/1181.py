def a(b, c):
    uw = set(c)
    
    sw = sorted(uw, key=lambda x: (len(x), x))
    
    return sw

b = int(input().strip())
c = [input().strip() for _ in range(b)]

result = a(b, c)
print("\n".join(result))
