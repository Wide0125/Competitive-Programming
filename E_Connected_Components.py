n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split)
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    todo = [i]
    while todo:
        curr = todo.pop()
        
