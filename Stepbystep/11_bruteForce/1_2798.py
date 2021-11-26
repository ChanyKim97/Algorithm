n, des = map(int, input().split())
card = list(map(int, input().split()))

sum_ = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = card[i] + card[j] + card[k]
            if temp<=des and temp>sum_:
                sum_ = temp

print(sum_)