def M(arr):
    arr.sort()
    n = len(arr)
    m = float('inf')

    for i in range(n):
        j = i
        while j < n and arr[j] - arr[i] <= 4:
            j += 1
        N = 5 - (j - i)
        m = min(m, N)

    return m
n = int(input())
arr = [int(input()) for _ in range(n)]

print(M(arr))