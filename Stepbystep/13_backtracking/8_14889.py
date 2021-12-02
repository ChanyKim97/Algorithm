N = int(input())

score = []
for i in range(N):
    temp = list(map(int,input().split()))
    score.append(temp)

team_list = []
another_team_list = []
min_ = 1e9
sum_start = 0
sum_link = 0

def dfs(start):
    global min_,sum_start,sum_link

    if len(team_list) == N//2:
        for i in range(N):
            if i+1 in team_list:
                continue
            another_team_list.append(i+1)

        for i in range(N//2):
            for j in range(i+1, N//2):
                sum_start += score[team_list[i]-1][team_list[j]-1]+score[team_list[j]-1][team_list[i]-1]
                sum_link += score[another_team_list[i]-1][another_team_list[j]-1]+score[another_team_list[j]-1][another_team_list[i]-1]

        if min_> abs(sum_start - sum_link):
            min_= abs(sum_start - sum_link)

        sum_start = 0
        sum_link = 0
        another_team_list.clear()
        return

    for i in range(start, N+1):
        if i not in team_list:
            team_list.append(i)
            dfs(i+1)
            team_list.pop()

dfs(1)
print(min_)