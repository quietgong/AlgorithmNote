n = int(input())
arr = list(map(int, input().split()))
dp=[0]*len(arr)
dp[0]=arr[0]
for i in range(1,n):
    dp[i]=max(dp[i-1]+arr[i], arr[i]) # 포인트
print(max(dp))

# DP 문제는 DP 테이블과 똑같은 크기의 수열을 자주 활용
# dp[i]=max(dp[i-1]+arr[i], arr[i]) 이전까지 더한값과 현재값을 더한 값, 현재값 비교