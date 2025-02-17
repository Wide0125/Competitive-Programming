for a in range(10):
    p, c = map(int, input().split())
    if p == 0 and c == 0:
        break
    adj = [[] for _ in range(p)]
    connections = []
    for i in range(c):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        connections.append([a, b])
    ans = False
    for i in connections:
        todo = [0]
        visited = [False] * p
        while todo:
            curr = todo.pop()
            if not visited[curr]:
                visited[curr] = True
                for next in adj[curr]:
                    if not [curr, next] == i and not [next, curr] == i:
                        todo.append(next)
        if set(visited) != set([True]):
            ans = True
    if ans:
        print("Yes")
    else:
        print("No")
    