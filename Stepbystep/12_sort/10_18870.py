N = int(input())
list_ = list(map(int, input().split()))
list_no_dup = sorted(list(set(list_)))

# for i in list_:
#     print(list_no_dup.index(i), end=' ')
# 시간초과

dic = {list_no_dup[i]:i for i in range(len(list_no_dup))}

for i in list_:
    print(dic[i], end=' ')