N = int(input())

cnt = 0
i = 0
while True:
    if '666' in str(i):
        cnt += 1
        if cnt == N:
            break
    i+=1

print(i)