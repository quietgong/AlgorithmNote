# 구현은 쉬우나 아이디어 떠올리는데 시간이 걸림
fib = [0] * 41
fib[0] = 0
fib[1] = 1
for i in range(2, len(fib)):
 fib[i] = fib[i-1] + fib[i-2]

T = int(input())

for _ in range(T):
 n = int(input())
 if n==0:
  print("1 0")
 else:
  print(fib[n-1], end=' ')
  print(fib[n])