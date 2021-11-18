max= -1
where = 0
for i in range(9):
    N = int(input())
    if max<N:
        where = i+1
        max = N

print(max)
print(where)