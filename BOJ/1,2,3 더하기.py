MAX = 11
d = [0] * MAX
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, MAX):
    d[i] = d[i - 1] + d[i - 2] + d[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])

# 경우의 수 덧셈문제, A(5) = 1 + A(4), 2 + A(3), 3 + A(2)
# 따라서, A(n)경우의수 = A(n-1)경우의수 + A(n-2)경우의수 + A(n-3)경우의수