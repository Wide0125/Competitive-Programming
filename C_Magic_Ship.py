x1, y1 = map(int, input().split())
x2, y2, = map(int, input().split())
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


def check(days):
    
    