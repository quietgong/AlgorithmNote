def lcm(a,b):
    m=a
    n=b
    while b!=0:
        r=a%b
        a=b
        b=r
    gcd=a
    return gcd*(m//gcd)*(n//gcd)

def solution(arr):
    for i in range(len(arr)-1):
        arr[i+1]=lcm(arr[i],arr[i+1])
    return arr[-1]

# 여러 수의 최소 공배수는 (a,b,c,d,e)
# lcm(lcm(lcm(a,b),b),c)...