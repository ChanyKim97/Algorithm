n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))
    dp[i].insert(0,0)
    dp[i].append(0)

for i in range(1,n):
    for j in range(1,len(dp[i])-1):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))