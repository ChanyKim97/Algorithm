T = int(input())

def checkprime(num):
    for i in range(2,num):
        if num%i == 0:
            break
            return False
    else:
        return True

for i in range(T):
    n = int(input())
    prime = 0
    for j in range(n//2, 1, -1):
        if checkprime(j) == True:
            if checkprime(n-j) == True:
                prime = j
                break

    print(j, n-j)