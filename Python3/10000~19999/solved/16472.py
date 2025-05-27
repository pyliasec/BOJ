def m(n, s):
    c = {}
    l = 0
    m = 0
    for r in range(len(s)):
        c[s[r]] = c.get(s[r], 0) + 1
        while len(c) > n:
            c[s[l]] -= 1
            if c[s[l]] == 0:
                del c[s[l]]
            l += 1
        m = max(m, r - l + 1)
    return m

n = int(input())
s = input().strip()
print(m(n, s))