import sys

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            col[x] = i
            if check(x):
                dfs(x+1)

n = int(sys.stdin.readline())
col = [0] * n
cnt = 0

dfs(0)
sys.stdout.write(str(cnt))