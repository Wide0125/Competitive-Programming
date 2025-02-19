import sys, os.path
if(os.path.exists('angry.in')):
    sys.stdin = open("angry.in", "r")
    sys.stdout = open("angry.out", "w")

N, K = map(int, input().split())
bales = sorted([int(input()) for _ in range(N)])


def valid(x):
    prev_range = -1
    cow_count = 0
    for i in bales:
        if i > prev_range:
            prev_range = i + 2 * x
            cow_count += 1
    return cow_count <= K


left = 0
right = N
while left < right:
    mid = (left + right) // 2
    if valid(mid):
        right = mid
        ans = mid
    else:
        left = mid + 1
print(ans)
