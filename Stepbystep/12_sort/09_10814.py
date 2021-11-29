import sys

N =int(input())

list_ = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    list_.append([age, name])

list_.sort(key=lambda x : x[0])

for i in list_:
    print(i[0], i[1])