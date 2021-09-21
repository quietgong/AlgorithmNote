n = int(input())
d = [0] * 301
a = [0] * 301
for i in range(n):
    a[i]=int(input())
d[0] = a[0]
d[1] = a[0]+a[1]
d[2] = max(a[1]+a[2], a[0]+a[2])
for i in range(3, n):
    d[i] = max(d[i - 3] + a[i - 1] + a[i], d[i - 2] + a[i])
print(d[n-1])

# 마지막 계단은 꼭 밟아야 하므로
# 1. 마지막 계단의 전 계단을 밟은 경우와
# 2. 마지막 계단의 전 계단을 밟지 않은 경우가 있다.