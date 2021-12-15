N = int(input())

s = []
for i in range(N):
    s.append(list(map(int, input().split())))

dp = [0 for i in range(N)]
s.sort(key=lambda s : s[0])

s_b = []
for i in range(N):
    s_b.append(s[i][1])
cnt = 0
for i in range(N):
    for j in range(i):
        if s_b[i]>s_b[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i]+=1

print(N - max(dp))