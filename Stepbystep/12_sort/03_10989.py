import sys
N = int(input())

list_ = [0 for i in range(10000)]

for i in range(N):
    n = int(sys.stdin.readline())
    list_[n-1] += 1

for i in range(len(list_)):
    if list_[i] != 0:
        for j in range(list_[i]):
            sys.stdout.write(str(i+1)+'\n')