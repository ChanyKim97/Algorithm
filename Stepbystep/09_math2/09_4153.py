while True:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 :
        break

    list_ = [a,b,c]
    max_ = max(list_)
    list_.remove(max_)

    if max_**2 == list_[0]**2 + list_[1]**2:
        print('right')
    else:
        print('wrong')