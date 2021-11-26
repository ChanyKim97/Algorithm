N = int(input())

man_list = []
for i in range(N):
    info = list(map(int, input().split()))
    man_list.append(info)

for i in man_list:
    rank = 1
    for j in man_list:
        if i[0] < j[0] and i[1]<j[1]:
            rank += 1
    print(rank, end=" ")

