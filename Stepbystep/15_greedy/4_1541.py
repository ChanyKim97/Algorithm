a = input().split('-')

# 조합으로 잘못생각함
# minus_cnt = len(a) - 1
#
# n = []
# for i in a:
#     if '+' in i:
#         tmp = i.split('+')
#         for j in tmp:
#             n.append(int(j))
#     else:
#         n.append(int(i))
#
# n.sort(reverse=True)
# sum = 0
# cnt = 1
# for i in n:
#     if cnt <= minus_cnt:
#         sum -= i
#         cnt += 1
#     else:
#         sum += i
#
# print(sum)

sum = 0
cnt = 0

for i in a:
    tmp = 0
    if "+" in i:
        for j in i.split('+'):
            tmp += int(j)
    else:
        tmp += int(i)

    if cnt == 0:
        sum+= tmp
        cnt+=1
    else:
        sum -= tmp

print(sum)