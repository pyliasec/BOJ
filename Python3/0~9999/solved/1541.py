def c(e):
    g2 = e.split('-')
    
    result = 0
    for i, g1 in enumerate(g2):
        g3 = sum(map(int, g1.split('+')))
        
        if i == 0:
            result += g3
        else:
            result -= g3
    return result

e = input().strip()
print(c(e))