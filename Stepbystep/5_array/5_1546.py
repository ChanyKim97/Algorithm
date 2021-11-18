N = int(input())
score = list(map(int, input().split()))

max = max(score)
sum = sum(score)
print(sum/max*100/N)