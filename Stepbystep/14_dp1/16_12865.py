N, K = map(int, input().split())

kg = [0]
v = [0]
for i in range(N):
    kg_, v_ = map(int, input().split())
    kg.append(kg_)
    v.append(v_)

dp = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= kg[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - kg[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
