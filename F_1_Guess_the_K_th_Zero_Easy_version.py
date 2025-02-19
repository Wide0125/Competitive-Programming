n, t = map(int, input().split())


def query(mid):
    print(f"? 0 {mid}")
    print()
    sum = int(input())
    return mid - sum < k


for a in range(t):
    k = int(input())
    input()
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if query(mid):
            left = mid
        else:
            right = mid
    print(right)
exit()