import sys
import math
def euclid(a,b):
    while True:
        r = a%b
        a = b
        b = r
        if r==0:
            break
    return a

n = int(input())
arr = [0]*n
res = []
ans = []
for i in range(n):
    arr[i] = int(sys.stdin.readline())

gcd = abs(arr[1]-arr[0])

for i in range(2, n):
    gcd = euclid(gcd, abs(arr[i]-arr[i-1]))

for i in range(2, int(math.sqrt(gcd))+1):
    if gcd%i==0:
        ans.append(i)
        ans.append(gcd//i)
ans.append(gcd)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i, end=' ')

# 포인트 : 유클리드 호제법, a[i+1]-a[i], a[i+2]-a[i+1] ... 의 최대공약수, 약수를 구할 때 제곱근까지만(제곱수일 때 중복제거, 어떤 수를 약수로 나눈 값도 추가)