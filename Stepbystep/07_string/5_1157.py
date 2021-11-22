S = input().upper()

check_list =[]
for i in range(26):
    check_list.append(0)

for s in S:
    check_list[ord(s) - ord('A')] += 1

max = max(check_list)

if(check_list.count(max) > 1):
    print('?')
else:
    index = check_list.index(max)
    print(chr(ord('A')+ index))