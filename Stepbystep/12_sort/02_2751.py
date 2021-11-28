#파이썬은 기본 정렬함수가 nlogn임
import sys

N = int(input())

list_ = []
for i in range(N):
    list_.append(int(sys.stdin.readline()))

for i in sorted(list_):
    sys.stdout.write(str(i)+'\n')