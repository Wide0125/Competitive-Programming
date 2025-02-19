n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))


def check(r):
    tower = 0
    city = 0
    while city < n and tower < m:
        if towers[tower] < city - r:
            tower += 1
        elif towers[tower] > city + r:
            return False
        else:
            city += 1
    return True


left = 0
right = int(1e9)
while left < right:
    mid = (left + right + 1) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(right)
