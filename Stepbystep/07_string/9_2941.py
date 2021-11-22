S = input()

cro_aplha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
for s in cro_aplha:
    S = S.replace(s, " ")

print(len(S))