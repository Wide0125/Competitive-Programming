import sys, os.path
if(os.path.exists('convention.in')):
    sys.stdin = open("convention.in", "r")
    sys.stdout = open("convention.out", "w")

N, M, C = map(int, input().split())
arrivals = sorted(list(map(int, input().split())))


def check_wait(x):
    curr_start = arrivals[0]
    available_buses = M
    available_seats = C - 1
    for cow in arrivals[1:]:
        if cow - curr_start <= x and available_seats > 0:
            available_seats -= 1
        else:
            available_buses -= 1
            curr_start = cow
            available_seats = C - 1
    return available_buses - 1 >= 0


left = 0
right = int(1e9)
while left < right:
    mid = (left + right) // 2
    if check_wait(mid):
        right = mid
        ans = mid
    else:
        left = mid + 1
print(ans)