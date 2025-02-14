t = int(input())
for a in range(t):
    n = int(input())
    neighbors = list(map(int, input().split()))
    adj = [set() for _ in range(n)]
    for i in range(n):
        a = i
        b = neighbors[i] - 1
        adj[a].add(b)
        adj[b].add(a)
    adj = list(map(list, adj))
    min_d = 0
    open_exists = False
    max_d = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        todo = [i]
        open = False
        while todo:
            curr = todo.pop()
            if visited[curr]:
                continue
            visited[curr] = True
            if len(adj[curr]) == 1:
                open = True
            for next in adj[curr]:
                todo.append(next)
        if not open:
            min_d += 1
        else:
            open_exists = True
        max_d += 1
    if open_exists:
        min_d += 1
    print(f"{min_d} {max_d}")
                