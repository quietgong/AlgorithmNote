MAX = 101
d = [0] * MAX
d[0] = 1
d[1] = 1
d[2] = 1
for i in range(3, MAX):
    d[i] = d[i-2] + d[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n-1])

# 수학적인 dp