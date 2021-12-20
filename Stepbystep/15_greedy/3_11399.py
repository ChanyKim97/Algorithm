N = int(input())

t = list(map(int, input().split()))
t.sort()

g = []
g.append(t[0])
for i in range(1, N):
    g.append(g[i-1] + t[i])

print(sum(g))