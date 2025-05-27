p = int(input())
time = list(map(int, input().split()))
time.sort()
r = 0
for i in range(len(time)):
    r += time[i]*p
    p -=1
print(r)