x1, y1 = map(int, input().split())
x2, y2, = map(int, input().split())
distance_ud = y2 - y1
distance_lr = x2 - x1
n = int(input())
forecast = input()
wind_ud = 0
wind_lr = 0
for wind in forecast:
    if wind =='U':
        wind_ud += 1
    elif wind == 'D':
        wind_ud -= 1
    elif wind == 'R':
        wind_lr += 1
    else:
        wind_lr -=1
found = False


def check(days, wind_ud, wind_lr):
    cycles = days // n
    wind_ud *= cycles
    wind_lr *= cycles
    for wind in forecast[: days % n]:
        if wind =='U':
            wind_ud += 1
        elif wind == 'D':
            wind_ud -= 1
        elif wind == 'R':
            wind_lr += 1
        else:
            wind_lr -= 1
    days -= abs(distance_ud - wind_ud)
    days -= abs(distance_lr - wind_lr)
    return days >= 0


left = 0
right = abs(distance_ud * n) + abs(distance_lr * n) + 1
while left < right:
    mid = (left + right) // 2
    if check(mid, wind_ud, wind_lr):
        right = mid
        found = True
    else:
        left = mid + 1
if found:
    print(right)
else:
    print(-1)
