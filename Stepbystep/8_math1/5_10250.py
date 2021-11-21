n = int(input())

for i in range(n):
    H, W, N = map(int, input().split())

    h = N%H
    if h == 0:
        h = H

    if N%H == 0:
        w = N//H
    else:
        w = N // H + 1

    if len(str(w)) == 1:
        print(f"{h}0{w}")
    else:
        print(f"{h}{w}")