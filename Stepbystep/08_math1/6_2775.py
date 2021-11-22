T = int(input())

def cal(k,n):
    list_ = [[0]*n for i in range(k+1)]

    for i in range(n):
        list_[0][i] = i+1

    for i in range(1,k+1):
        sum = list_[i-1][0]
        for j in range(n):
            list_[i][j] = sum
            if j == n-1:
                break
            sum += list_[i-1][j+1]

    return list_[k][n-1]

for i in range(T):
    k = int(input())
    n = int(input())

    print(cal(k, n))