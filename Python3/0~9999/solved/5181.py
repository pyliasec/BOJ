def t(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def o(a, b, c, d):
    return a < d and c < b

import sys

def main():
    I = sys.stdin.read().strip().splitlines()
    if not I:
        return
    i = 0
    K = int(I[i].strip())
    i += 1
    for D in range(1, K + 1):
        m, n = map(int, I[i].split())
        i += 1
        C = {}
        for _ in range(m):
            p = I[i].split()
            i += 1
            a = p[0]
            b = p[1]
            c = p[2]
            s, e = c.split('-')
            C[a] = (b, t(s), t(e))
        x = 0
        for _ in range(n):
            L = I[i].split()
            i += 1
            f = False
            for j in range(len(L)):
                for k in range(j + 1, len(L)):
                    d1, s1, e1 = C[L[j]]
                    d2, s2, e2 = C[L[k]]
                    if d1 == d2 and o(s1, e1, s2, e2):
                        f = True
                        break
                if f:
                    break
            if f:
                x += 1
        print(f"Data Set {D}:")
        print(x)

if __name__ == '__main__':
    main()