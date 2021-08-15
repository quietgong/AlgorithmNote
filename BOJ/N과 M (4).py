from itertools import combinations_with_replacement
import sys
N,M = map(int, sys.stdin.readline().split())
arr = [0]*N
ans = []
for i in range(N):
    arr[i] = i+1

ans = list(combinations_with_replacement(arr, M))
for i in range(len(ans)):
    print(str(ans[i]).replace("(","").replace(")","").replace(",",""))