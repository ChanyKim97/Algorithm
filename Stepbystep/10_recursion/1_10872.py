N = int(input())

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return factorial(num-1) * num

print(factorial(N))