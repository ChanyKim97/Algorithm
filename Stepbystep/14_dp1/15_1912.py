N = int(input())

n = list(map(int, input().split()))

dp = [0 for i in range(N)]
dp[0] = n[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] + n[i], n[i])

print(max(dp))