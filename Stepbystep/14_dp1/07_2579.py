n = int(input())

stair = []
dp = []

for i in range(n):
    stair.append(int(input()))

if n == 1:
    dp.append(stair[0])
elif n == 2:
    dp.append(stair[0])
    dp.append(max(stair[1], stair[0] + stair[1]))
else:
    dp.append(stair[0])
    dp.append(max(stair[1], stair[0]+stair[1]))
    dp.append(max(stair[0]+stair[2], stair[1]+stair[2]))
    for i in range(3,n):
        #i번째 계단오는 방법
        #두칸전 최대값 + 현재 나의값으로
        #세칸전 최대값 + 전 계단값+ 현재 내 계단값
        dp.append(max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i]))

print(dp[-1])