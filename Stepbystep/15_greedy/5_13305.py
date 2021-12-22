N = int(input())

dis = list(map(int, input().split()))
pri = list(map(int, input().split()))

total = 0

tmp_pri = pri[0]
total += tmp_pri * dis[0]

for i in range(1, len(dis)):
    if tmp_pri > pri[i]:
        tmp_pri = pri[i]

    total += tmp_pri * dis[i]

print(total)