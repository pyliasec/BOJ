import sys
import heapq

input = sys.stdin.readline
n = int(input())
h = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(h) < n:
            heapq.heappush(h, num)
        else:
            if num > h[0]:
                heapq.heappushpop(h, num)

print(h[0])