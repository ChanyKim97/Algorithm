import math
T = int(input())

for t in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(float, input().split())
    dis = math.sqrt((x_1- x_2)**2 + (y_1-y_2)**2)
    max_r = max(r_1,r_2)
    min_r = min(r_1,r_2)

    if dis == 0:
        if r_1 == r_2:
            print(-1)
        else:
            print(0)
    else:
        if r_1+r_2 < dis:
            print(0)
        elif (r_1 + r_2) == dis or max_r == dis + min_r:
            print(1)
        elif r_1 + r_2 >dis and max_r < dis+min_r:
            print(2)
        else:
            print(0)