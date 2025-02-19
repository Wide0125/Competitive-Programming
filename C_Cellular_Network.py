n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))


def check(r):
    tower = 0
    city = 0
    while city < n and tower < m:
        if towers[tower] < cities[city] - r:
            tower += 1
        elif towers[tower] > cities[city] + r:
            return False
        else:
            city += 1
    return city == n


left = 0
right = int(2e9)
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(right)
