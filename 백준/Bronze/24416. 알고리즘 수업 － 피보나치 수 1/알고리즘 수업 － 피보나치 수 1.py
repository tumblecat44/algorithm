n = int(input())
dp = [0 for _ in range(n)]
dp[0:2] = [0,1,1]
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[-1],n-2)