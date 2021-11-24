N = int(input())

def hanoi(N,first,second,third):
    if N == 1:
        print(first, third)
    else:
        #첫기둥 한개 제외 나머지 두번째 기둥으로
        hanoi(N-1, first, third, second)
        print(first, third)
        hanoi(N-1, second, first, third)


print(2**N -1)

hanoi(N, 1, 2, 3)