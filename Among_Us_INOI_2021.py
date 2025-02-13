T = int(input())
for a in range(T):
    N, Q = map(int, input().split())
    adj = [[] for _ in range(N)]
    for i in range(Q):
        temp, a, b = map(int, input().split())
        adj[a - 1].append([temp, b - 1])
        adj[b - 1].append([temp, a - 1])
    teams = [0] * N
    ans = 0
    impossible = False
    for i in range(N):
        count1 = 0
        count2 = 0
        if teams[i]:
            continue
        teams[i] = 1
        count1 += 1
        todo = [i]
        while todo:
            curr = todo.pop()
            for j in adj[curr]:
                SD, next = j
                if SD == 1:
                    if not teams[next]:
                        if teams[curr] == 1:
                            teams[next] = 2
                            count2 += 1
                        else:
                            teams[next] = 1
                            count1 += 1
                        todo.append(next)
                    elif teams[next] == teams[curr]:
                        impossible = True
                        break
                else:
                    if not teams[next]:
                        if teams[curr] == 1:
                            teams[next] = 1
                            count1 += 1
                        else:
                            teams[next] = 2
                            count2 += 1
                        todo.append(next)
                    elif teams[next] != teams[curr]:
                        impossible = True
                        break
        if impossible:
            break
        ans += max(count1, count2)
    if impossible:
        print(-1)
    else:
        print(ans)
