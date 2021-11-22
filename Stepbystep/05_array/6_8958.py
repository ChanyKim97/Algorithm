N = int(input())

for i in range(N):
    result = list(input())
    sum = 0
    add_num = 1
    for OX in result:
        if OX == "O":
            sum += add_num
            add_num += 1
        else:
            add_num = 1
    print(sum)
