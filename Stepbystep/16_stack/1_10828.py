import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    c = sys.stdin.readline().split()

    if c[0] == 'push':
        stack.append(int(c[1]))

    if c[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    if c[0] == 'size':
        print(len(stack))

    if c[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if c[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

