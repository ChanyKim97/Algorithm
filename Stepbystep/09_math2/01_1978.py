N = int(input())

list_ = list(map(int, input().split()))

count = 0

for num in list_:
    if num == 1:
        continue
    else:
        count += 1
        for j in range(2,num):
            if num % j == 0:
                count -= 1
                break


print(count)