def GCD(a, b):
    gcd = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

t = int(input())
arr = list(map(int, input().split()))
a1 = arr[0]
n = 0
for i in range(1, len(arr)):
    n = GCD(a1, arr[i])
    print(f"{a1//n}/{arr[i]//n}")