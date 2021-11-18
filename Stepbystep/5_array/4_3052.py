num = list()
for i in range(10):
    N = int(input())
    N =N%42
    num.append(N)

num = set(num)
print(len(num))