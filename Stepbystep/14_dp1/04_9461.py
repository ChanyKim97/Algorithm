N = int(input())

list_ = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(11, 101):
    list_.append(list_[i-1] + list_[i-5])

for i in range(N):
    n = int(input())
    print(list_[n])