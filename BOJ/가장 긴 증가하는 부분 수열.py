n = int(input())
arr = list(map(int, input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
print(max(dp))

# 1. 조건 arr[i] > arr[j] : 증가하는 부분 수열이여야 하므로, arr의 원소가 더 클 때 조건에 충족하게 설정
# 2. 조건 dp[i] < dp[j]+1 : arr[i]를 추가했을 때(dp[j]+1) i까지의 길이보다 크다면 dp[i]를 dp[j]+1로 갱신