N = int(input())
M = 0

for i in range(1,N):
    a = list(map(int, str(i)))
    sum_ = i + sum(a)
    if sum_ == N:
        M = i
        break

print(M)