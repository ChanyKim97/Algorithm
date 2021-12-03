T = int(input())
#not dp
#cnt_0 = 0
#cnt_1 = 0
#
#def fibonacci(n):
#    global cnt_1, cnt_0
#    if n == 0:
#        cnt_0 += 1
#        return 0
#    elif n == 1:
#        cnt_1 += 1
#        return 1
#    else:
#        return fibonacci(n-1)+fibonacci(n-2)


#for i in range(T):
#    n = int(input())
#   fibonacci(n)
#    print(cnt_0, cnt_1)
#    cnt_0 = 0
#    cnt_1 = 0

zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
    if len(zero)<=n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-2]+zero[i-1])
            one.append(one[i-2]+one[i-1])
    print(zero[n], one[n])

for i in range(T):
    n = int(input())
    fibo(n)