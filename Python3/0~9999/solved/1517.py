def a(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    l, lc = a(arr[:mid])
    r, rc = a(arr[mid:])
    m, mc = b(l, r)
    return m, lc + rc + mc

def b(l, r):
    m, c, i, j = [], 0, 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            m.append(l[i])
            i += 1
        else:
            m.append(r[j])
            j += 1
            c += len(l) - i
    return m + l[i:] + r[j:], c

N = int(input())
arr = list(map(int, input().split()))
_, count = a(arr)
print(count)
