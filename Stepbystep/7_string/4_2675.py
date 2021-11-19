N = int(input())

for i in range(N):
    re, S = map(str, input().split())
    re = int(re)
    for s in S:
        print(s*re, end="")
    print("")