N = input()
list_ = []

for i in N:
    list_.append(int(i))

for i in sorted(list_, reverse=True):
    print(i, end='')