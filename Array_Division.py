n, k = map(int, input().split())
array = list(map(int, input().split()))


def check(max_sum):
    subarrays = 1
    element = 0
    curr_sub = 0
    while subarrays < k and element < n:
        if curr_sub + array[element] <= max_sum:
            curr_sub += array[element]
            element += 1
        elif array[element] <= max_sum:
            curr_sub = array[element]
            subarrays += 1
            element += 1
        else:
            return False
    return element == n and subarrays == k


left = 0
right = sum(array)
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(right)