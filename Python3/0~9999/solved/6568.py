import sys

def s():
    m = []
    for _ in range(32):
        line = sys.stdin.readline().strip()
        if not line:
            return None
        m.append(int(line, 2))
    
    a = p = 0

    while True:
        i = m[p]
        o, x = divmod(i, 32)
        p = (p + 1) % 32

        if o == 0:
            m[x] = a
        elif o == 1:
            a = m[x]
        elif o == 2:
            if a == 0:
                p = x
        elif o == 3:
            pass
        elif o == 4:
            a = (a - 1) & 255
        elif o == 5:
            a = (a + 1) & 255
        elif o == 6:
            p = x
        elif o == 7:
            break

    return format(a, '08b')

def m():
    while True:
        r = s()
        if r is None:
            break
        print(r)

if __name__ == "__main__":
    m()