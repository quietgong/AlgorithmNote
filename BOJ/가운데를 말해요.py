import sys
import heapq
input=sys.stdin.readline
left=[]
right=[]
N=int(input())
for i in range(N):
    x=int(input())
    if len(left)==len(right):
        heapq.heappush(left,-x)
    else:
        heapq.heappush(right,x)

    if len(left)>=1 and len(right)>=1 and left[0]*-1 > right[0]:
        a=heapq.heappop(left)*-1
        b=heapq.heappop(right)
        heapq.heappush(left,-b)
        heapq.heappush(right,a)
    print(-left[0])

# 두 개의 힙 사용
# 파이썬에서 최대힙 사용
# left의 루트가 right의 루트보다 클 때 스위칭