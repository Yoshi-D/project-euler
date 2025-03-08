n=100
dp  = [0] * (n+1)
dp[0] = 1

for num in range(1,n):
   for i in range(num,n+1):
      dp[i] += dp[i-num]
print(dp[n])
