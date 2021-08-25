import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
a = sorted(list(set(arr)))
dic = {a[i]: i for i in range(len(a))}

for i in arr:
    print(dic[i], end=' ')

# 포인트 : set, sorted, dict의 시간복잡도