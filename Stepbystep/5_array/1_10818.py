N = int(input())
num_list = list(map(int,input().split()))

# min = 1000000
# max = -1000000
# for num in num_list:
#     if num<min:
#         min = num
#     if num>max:
#         max = num
#
# print(min, max)

num_list.sort()

print(num_list[0], num_list[-1])