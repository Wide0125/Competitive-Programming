n, k = map(int, input().split())
array = sorted(list(map(int, input().split())))


def med_reachable(x):
    ops_needed = 0
    for i in range((n - 1) // 2, n):
        ops_needed += max(0, x - array[i])
    return ops_needed <= k


left = 1
right = int(2e9) + 1
while left < right:
    mid = (left + right) // 2
    if med_reachable(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid
print(ans)
