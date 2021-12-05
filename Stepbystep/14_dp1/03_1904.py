# 1
# 00 11
# 100 001 011
# 0000 1100 1001 0011 0111

N = int(input())

dp = [0]* 1000001

dp[1]=1
dp[2]=2

for i in range(3, N+1):
    dp[i] = (dp[i-1]+ dp[i-2]) % 15746

print(dp[N])