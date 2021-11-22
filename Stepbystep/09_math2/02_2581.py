M = int(input())
N = int(input())

list_ = []
for num in range(M, N+1):
    if num == 1:
        continue
    else:
        list_.append(num)
        for i in range(2,num):
            if num % i == 0:
                list_.remove(num)
                break

if len(list_)< 1 :
    print(-1)
else:
    print(sum(list_))
    print(min(list_))