n = int(input())

finish = 1
add = 2

while True:
    if n > finish:
        finish += add
        add += 1
    else:
        break

if (add - 1)%2 == 0:
    print(f"{add - 1 - (finish -n)}/{add - (add - 1 - (finish -n))}")
else:
    print(f"{add- (add - 1 - (finish - n))}/{(add - 1 - (finish - n))}")