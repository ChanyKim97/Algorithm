import sys

N = int(input())

list_ = []
for i in range(N):
    list_.append(sys.stdin.readline().strip())

list_set = set(list_)
list_=list(list_set)

list_.sort()
list_.sort(key=len)

for i in list_:
    print(i)