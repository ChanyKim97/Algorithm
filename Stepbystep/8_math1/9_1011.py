T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance =y-x

    move = 1
    count = 0
    move_sum = 0

    while move_sum < distance:
        count+=1
        move_sum += move
        if count%2 == 0:
            move+=1

    print(count)