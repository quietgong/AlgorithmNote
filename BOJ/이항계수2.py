fac = [0] * 1001
fac[0] = 1
fac[1] = 1
for i in range(2, 1001):
    fac[i] = i * fac[i - 1]

n, k = map(int, input().split())
ans = int(fac[n] // (fac[k] * fac[n - k]))
print(ans % 10007)

# 포인트 : 이항계수(n k)의 공식 : n! / (k!(n-k)!)