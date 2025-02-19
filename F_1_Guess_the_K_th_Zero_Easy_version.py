n, t = map(int, input().split())


def query(mid):
    print(f"? 1 {mid}")
    sum = int(input())
    return mid - sum <= k


k = int(input()) - 1
left = 0
right = n
while left < right - 1:
    mid = (left + right) // 2
    if query(mid):
        left = mid
    else:
        right = mid
print(f"! {right}")
