def a(b, c, d):
    c.sort()
    count = 0

    for start in range(1, 1001):
        for end in range(start + 1, 1002):
            if start <= d <= end:
                valid = True
                for x in range(start, end + 1):
                    if x in c:
                        valid = False
                        break
                if valid:
                    count += 1

    return count

b = int(input().strip())
c = list(map(int, input().strip().split()))
d = int(input().strip())

result = a(b, c, d)
print(result)
