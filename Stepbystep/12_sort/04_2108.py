import sys
from collections import Counter

N = int(input())
list_ = []

for i in range(N):
    n = int(sys.stdin.readline())
    list_.append(n)

list_.sort()

cnt = Counter(list_).most_common(2)

print(round(sum(list_)/N))
print(list_[N//2])
if len(cnt)>1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(list_) - min(list_))