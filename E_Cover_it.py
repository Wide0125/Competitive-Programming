t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = [[_] for _ in range(n)]
    for a in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    todo = sorted([_ for _ in range(n)], key=lambda x: len(adj[x]), reverse=True)
    visited = [False] * n
    ans = []
    in_ans = [False] * n
    while todo:
        curr = todo.pop()
        if visited[curr]:
            continue
        ans.append(curr)
        in_ans[curr] = True
        for next in adj[curr]:
            visited[next] = True
    if len(ans) <= n // 2:
        print(len(ans))
        for a in range(len(ans)):
            print(ans[a] + 1, end=' ')
    else:
        print(n - len(ans))
        for a in range(n):
            if not in_ans[a]:
                print(a + 1, end=' ')
