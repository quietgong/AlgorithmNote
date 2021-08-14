N = int(input())
arr = list(map(int, input().split()))
arr.sort()
if N%2==0:
    print(arr[0]*arr[-1])
else:
    print( arr[N//2] ** 2)

# 진짜 약수 개수가 짝수인지, 홀수인지만 분류하면 쉽게 풀수있다.