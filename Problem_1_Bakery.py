def valid(w):
    lo, hi = max(1, ctime - w), min(ctime + mtime - w - 1, ctime)
    d = ctime + mtime - w
    for cow in friends:
        a, b, c = cow
        if a > b:
            hi = min(hi, (c - b * d) // (a - b))
        elif a < b:
            lo = max(lo, (c - b * d - (b - a - 1)) // (a - b))
        elif a * d > c:
            return False
    return lo <= hi

T = int(input())
for case in range(T):
    input()
    N, ctime, mtime = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(N)]
    left = 0
    right = ctime + mtime - 2
    while left < right:
        mid = (left + right) // 2
        if valid(mid):
            right = mid
        else:
            left = mid + 1
    print(right)
    