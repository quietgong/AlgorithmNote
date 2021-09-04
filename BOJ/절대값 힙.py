import sys
import heapq

input = sys.stdin.readline

heap=[]
n = int(input())
for _ in range(n):
    a = int(input())
    if a==0:
        if len(heap)==0:
            print("0")
        else:
            print(heapq.heappop(heap)[1])
    else:
        if a<0:
            heapq.heappush(heap, (abs(a),a))
        else:
            heapq.heappush(heap, (abs(a),a))
    
# 절대값 힙 (튜플 자료형 사용)