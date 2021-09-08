import sys

input = sys.stdin.readline
n, k = map(int, input().split())
cnt = 0
a = []
for i in range(n):
    a.append(int(input()))

for coin in a:
 count += coin//k
 k%=coin

print(cnt)

# 그리디, 동전의 거스름돈을 while, continue를 통해 구현한다.