N = int(input())

list_ = []
for i in range(N):
    x, y = map(int, input().split())
    list_.append([x,y])

list_.sort(key= lambda x:(x[0], x[1]))

for i in list_:
    print(i[0], i[1])