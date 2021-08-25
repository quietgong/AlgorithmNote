t = int(input())
for _ in range(t):
    p = 1
    fac = [0]*31
    fac[0]=1
    fac[1]=1
    for i in range(2,len(fac)):
        fac[i] = i*fac[i-1]
    r,n = map(int,input().split())

    for i in range(n-r+1, n+1):
        p = i*p

    print(p//fac[r])