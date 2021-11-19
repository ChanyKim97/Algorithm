# S = list(input())
#
# alpha_list = []
# for i in range(26):
#     alpha_list.append(-1)
#
# count = 0
# for check in S:
#     if alpha_list[ord(check) - ord('a')] == -1:
#         alpha_list[ord(check) - ord('a')] = count
#
#     count += 1
#
# for num in alpha_list:
#     print(num, end=" ")

#더 간단한 코드
s = input()
alphabet = list(range(ord('a'),ord('z')))

for x in alphabet:
    print(s.find(chr(x)), end=" ")