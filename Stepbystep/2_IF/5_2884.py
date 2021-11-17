hour, minute = map(int, input().split())

if(minute>=45):
    minute = minute-45
else:
    minute = minute+15
    if(hour>0):
        hour = hour - 1
    else:
        hour = 23

print(hour, minute)