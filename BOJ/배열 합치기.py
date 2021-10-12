a,b=map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
arr3=arr1+arr2
arr3.sort()
for i in arr3:
 print(i, end=' ')

# '+' 연산자를 통해 여러 리스트를 하나로 합칠 수 있다.