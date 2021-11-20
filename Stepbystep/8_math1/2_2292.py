n = int(input())

finish = 1
layer = 1
while True:
    if n <= finish:
        print(layer)
        break
    else:
        finish += (6*layer)
        layer+=1