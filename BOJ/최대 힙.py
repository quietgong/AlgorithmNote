import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(-(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -a)

# 최대힙