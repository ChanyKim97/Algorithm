N = int(input())

num = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_ = -1000000000
min_ = 1000000000

def dfs(depth, total, plus, minus, multi, divide):
    global max_, min_

    if depth == N:
        max_ = max(total, max_)
        min_ = min(total, min_)
        return

    if plus:
        dfs(depth+1, total + num[depth], plus - 1, minus, multi, divide)
    if minus:
        dfs(depth+1, total - num[depth], plus, minus - 1, multi, divide)
    if multi:
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multi, divide - 1)

dfs(1, num[0], oper[0], oper[1], oper[2], oper[3])
print(max_)
print(min_)