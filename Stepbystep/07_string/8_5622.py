s = input()

num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0
for i in s:
    for j in num:
        if i in j:
            result += num.index(j)+3

print(result)