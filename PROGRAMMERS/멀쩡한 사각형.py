# from math import gcd (최대 공약수)
def euclid(a,b):
    if a>b:
        a,b=b,a
    while b!=0:
        r=a%b
        a,b=b,r
    return a
    
def solution(w,h):
    return w*h-(w+h-euclid(w,h))

# 수학문제