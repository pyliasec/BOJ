def a(b):
    return f"{b:,.2f}"

while True:
    c = input().split()
    if c[0] == '-1':
        break
    
    d = list(map(float, c[:3]))
    e = int(c[3])
    
    for f in range(4, e + 1):
        g = round(d[-3] * d[-2] / d[-1], 2)
        d.append(g)
    
    h = d[e - 1]
    print(f"Month {e} cost: ${a(h)}")