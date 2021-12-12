N = int(input())

list_ = []

for i in range(N):
    s, f= map(int, input().split())
    list_.append([s,f])

list_ = sorted(list_, key=lambda a: a[0])
list_ = sorted(list_, key=lambda a: a[1])
#print(list_)

cnt = 0
finish = 0

for i, j in list_:
    if i>= finish:
        cnt += 1
        finish = j

print(cnt)