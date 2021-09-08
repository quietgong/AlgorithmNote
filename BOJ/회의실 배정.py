import sys
n = int(input())
a = [[0] * 2 for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().split()))
a.sort(key=lambda x:x[0])
a.sort(key=lambda x:x[1])
min_num = 0
ans=0
for i in range(n):
    if a[i][0]>=min_num:
        min_num=a[i][1]
        ans+=1
print(ans)