def self_num(num):
    num_str = list(str(num))
    sum = num
    for a in num_str:
        sum += int(a)
    return sum

self_num_list = list(range(1,10000))
# for i in range(10000):
#     self_num_list.append(i+1)


for i in range(10000):
    check_num = self_num(i+1)
    if check_num in self_num_list:
        self_num_list.remove(check_num)

for num in self_num_list:
    print(num)