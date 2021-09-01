n = int(input())
dp = [0]*100001
dp[0] = 3
dp[1] = 7
for i in range(2, 100001):
    dp[i] = (dp[i-1]*2 + dp[i-2]) % 9901
print(dp[n-1])

# 점화식 : 0일 때(dp[i-1] 경우의 수와 1과 2 일때의 경우(dp[i-2])의 수를 더해준다.