from itertools import product
import sys
N,M = map(int, sys.stdin.readline().split())
arr = [0]*N
ans = []
for i in range(N):
    arr[i] = i+1

ans = list(product(arr, repeat=M))
for i in range(len(ans)):
    print(str(ans[i]).replace("(","").replace(")","").replace(",",""))

# 포인트 : from itertools import productm, from itertools import combination_with_replacement