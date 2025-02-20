n = int(input())
field = list(input())
packmen = []
asterisks = []
for i in range(n):
    if field[i] == 'P':
        packmen.append(i)
    elif field[i] == '*':
        asterisks.append(i)


def check(time, packmen):
    time_left = [time] * len(packmen)
    curr_p = 0
    curr_a = 0
    while curr_p < len(packmen) and curr_a < len(asterisks):
        if asterisks[curr_a] < packmen[curr_p] - time_left[curr_p]:
            return False
        if asterisks[curr_a] > packmen[curr_p] + time_left[curr_p]:
            curr_p += 1
            continue
        temp = asterisks[curr_a]
        if asterisks[curr_a] >= packmen[curr_p]:
            curr_a += 1
            time_left[curr_p] -= min(time_left[curr_p], abs(packmen[curr_p] - temp))
            packmen[curr_p] = temp
            continue
        distance = packmen[curr_p] - temp
        if distance < time_left[curr_p] / 3:
            for i in range(curr_a, len(asterisks)):
                if asterisks[i] > packmen[curr_p] + (time_left[curr_p] - (distance * 2)):
                    break
                curr_a = i + 1
            time_left[curr_p] -= distance * 2
            if asterisks[curr_a - 1] > packmen[curr_p]:
                time_left[curr_p] -= asterisks[curr_a - 1] - packmen[curr_p]
        else:
            for i in range(curr_a, len(asterisks)):
                if asterisks[i] > packmen[curr_p] + (time_left[curr_p] - (packmen[curr_p] - temp)) // 2:
                    break
                curr_a = i + 1
            time_left[curr_p] -= distance
            if asterisks[curr_a - 1] > packmen[curr_p]:
                time_left[curr_p] -= (asterisks[curr_a - 1] - packmen[curr_p]) * 2
        packmen[curr_p] = temp
    return curr_a == len(asterisks)


left = 0
right = (n - 2) * 2 + 1
while left < right:
    mid = (left + right) // 2
    if check(mid, packmen.copy()):
        right = mid
    else:
        left = mid + 1
print(right)
