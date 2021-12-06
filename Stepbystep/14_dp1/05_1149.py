N = int(input())

dp =[]
for i in range(N):
    temp = list(map(int, input().split()))
    dp.append(temp)

for i in range(1,N):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))