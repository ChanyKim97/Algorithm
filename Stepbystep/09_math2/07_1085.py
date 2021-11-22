x, y, w, h = map(int, input().split())

list_ = [0, 0, w, h]
list_[0] = abs(x-list_[0])
list_[1] = abs(y-list_[1])
list_[2] = abs(x-list_[2])
list_[3] = abs(y-list_[3])

print(min(list_))