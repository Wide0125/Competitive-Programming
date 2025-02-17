import sys, os.path
if(os.path.exists('cowdance.in')):
    sys.stdin = open("cowdance.in", "r")
    sys.stdout = open("cowdance.out", "w")

N, Tmax = map(int, input().split())
intervals = [int(input()) for _ in range(N)]


def get_time(k):
    stage = intervals[:k]
    for cow in intervals[k: N]:
        stage.sort()
        stage[0] += cow
    return max(stage) <= Tmax
        


left = 0
right = N
while left < right:
    mid = (left + right) // 2
    if mid == 0:
        break
    if get_time(mid):
        right = mid
    else:
        left = mid + 1
        ans = mid
print(ans + 1)
