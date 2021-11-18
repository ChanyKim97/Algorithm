N = int(input())

for i in range(N):
    result = list(map(int, input().split()))
    avg = sum(result[1:])/result[0]
    count = 0
    for num in result[1:]:
        if num > avg:
            count += 1
    print(f"{count/result[0]*100:.3f}%")