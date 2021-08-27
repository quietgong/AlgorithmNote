import math

def is_prime(a,b):
    prime = [True] * (b+1)
    cnt=0
    for i in range(2, int(math.sqrt(b))+1):
        if prime[i]:
            for j in range(i*2, b+1, i):
                prime[j] = False

    for i in range(a+1, b+1):
        if prime[i]:
            cnt+=1
    print(cnt)
while True:
    n = int(input())
    res=0
    if n == 0:
        break

    is_prime(n, n*2)

# 포인트 : n이 소수인지 아닌지 판별하기 위해선 math.sqrt(n)까지 검사하면 된다.