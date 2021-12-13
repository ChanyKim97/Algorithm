N = int(input())
s = list(map(int,input().split()))

dp_A = [0 for i in range(N)]
dp_D = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if s[i]>s[j] and dp_A[i]<dp_A[j]:
            dp_A[i] = dp_A[j]
    dp_A[i]+=1

for i in range(N-1, -1 ,-1):
    for k in range(N-1, i, -1):
        if s[i]>s[k] and dp_D[i]<dp_D[k]:
            dp_D[i] = dp_D[k]
    dp_D[i]+=1


sum = []
for i in range(N):
    sum.append(dp_A[i] + dp_D[i] - 1 )

print(max(sum))