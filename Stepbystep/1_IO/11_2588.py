#엔터입력이면 두번 mapX
A= int(input())
B= int(input())

print(A*(B%10))
print(A*(B%100-B%10)//10)
print(A*(B//100))
print(A*B)