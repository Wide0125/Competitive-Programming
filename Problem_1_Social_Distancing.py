import sys, os.path
if(os.path.exists('socdist.in')):
    sys.stdin = open("socdist.in", "r")
    sys.stdout = open("socdist.out", "w")

N, M = map(int, input().split())
patches = sorted([list(map(int, input().split())) for _ in range(M)])


def distance_possible(x):
    prev_cow = patches[0][0]
    remaining_cows = N - 1
    curr_patch = 0
    while curr_patch < M and remaining_cows > 0:
        if prev_cow + x <= patches[curr_patch][1]:
            remaining_cows -= 1
            prev_cow += x
        elif curr_patch < M - 1 and patches[curr_patch + 1][1] >= prev_cow + x:
            curr_patch += 1
            remaining_cows -= 1
            prev_cow = max(prev_cow + x, patches[curr_patch][0])
        else:
            curr_patch += 1
    return remaining_cows == 0


left = 1
right = patches[-1][1] - patches[0][0]
while left < right:
    mid = (left + right) // 2
    if distance_possible(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid
print(ans)