N, M = map(int,input().split())

list_ = []
for i in range(N):
    list_.append(int(input()))

cnt = 0
for i in range(N-1, -1, -1):
    if M == 0:
        break
    if list_[i] > M:
        continue
    cnt += M // list_[i]
    M %= list_[i]

print(cnt)