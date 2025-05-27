def c(N, M, i1, i2):
    for i in range(N):
        r = ''.join([char * 2 for char in i1[i]])
        if r != i2[i]:
            return False
    return True

N, M = map(int, input().split())

i1 = [input().strip() for _ in range(N)]

i2 = [input().strip() for _ in range(N)]

if c(N, M, i1, i2):
    print("Eyfa")
else:
    print("Not Eyfa")