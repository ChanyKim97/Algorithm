N = int(input())

firstN = N
count = 0
while True:
    count = count + 1

    temp = N//10 + N%10
    new_N = (N%10)*10 + temp%10
    if(new_N == firstN):
        break

    N = new_N

print(count)