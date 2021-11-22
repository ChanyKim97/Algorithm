def check(num):
    num_list = list(str(num))
    if(len(num_list)<=2):
        return True
    else:
        diff = int(num_list[1]) - int(num_list[0])
        check_num = int(num_list[0])
        for a in num_list[1:]:
            if check_num+diff == int(a):
                check_num = int(a)
                continue
            else:
                return False
        return True

N = int(input())
count = 0
for i in range(1,N+1):
    if check(i) == True:
        count += 1

print(count)

# 참조 간단한 코드
# 문제에 1000이하라고 되어있어 3자리만 check한 경우임
# N = int(input())
# count = 0
#
# for n in range(1, N+1):
#     if n<= 99:
#         count += 1
#     else:
#         nums = list(map(int, str(n)))
#         if nums[0] - nums[1] == nums[1] - nums[2]:
#             count += 1
#
# print(count)