N = int(input())

dp = [0 for i in range(N+1)]

list_ = [0]
for i in range(N):
    list_.append(int(input()))


if N == 1:
    dp[N] = list_[1]
elif N == 2:
    dp[N] = list_[1]+ list_[2]
else:
    dp[1] = list_[1]
    dp[2] = list_[1] + list_[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], dp[i-2]+list_[i], dp[i-3]+list_[i-1]+list_[i])

print(dp[N])