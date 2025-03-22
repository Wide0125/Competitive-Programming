for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a, reverse=True)
    swap_loc = [None, None]
    swap_num = None
    for i in range(N):
        if a[i] != sorted_a[i]:
            swap_loc[1] = i
            swap_num = sorted_a[i]
            for j in range(i + 1, N):
                if a[j] == sorted_a[i]:
                    swap_loc[0] = j
            break
    if None not in swap_loc:
        a.insert(swap_loc[1], swap_num)
        a.pop(swap_loc[0] + 1)
    i = 0
    j = 0
    ans = []
    while i < N and j < N:
        if a[i] == sorted_a[j]:
            ans.append(a[i])
            j += 1
            i += 1
        else:
            i += 1
    print(*ans)
