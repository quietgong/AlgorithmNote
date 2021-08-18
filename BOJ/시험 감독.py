N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
ans=0
for i in range(len(arr)):
    arr[i] = arr[i]-B
    ans +=1
    if arr[i] > 0:
        ans += arr[i] // C
        if arr[i] % C > 0:
            ans += 1
print(ans)

# 포인트 : 수학적인 공식이 요구될수록 간단하고 명료하게 작성한다.