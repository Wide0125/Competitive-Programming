n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
adj = [[] for _ in range(n)]
adj_matrix = [[False] * n for _ in range(n)]
for i in edges:
    a = i[0] - 1
    b = i[1] - 1
    adj[a].append(b)
    adj[b].append(a)
teams = [0] * n

todo = [0]
teams[0] = 1
while todo:
    curr = todo.pop()
    for next in adj[curr]:
        if not teams[next]:
            teams[next] = 2 if teams[curr] == 1 else 1
            todo.append(next)
ans = 0
count1 = teams.count(1)
count2 = teams.count(2)
for i in range(n):
    if teams[i] == 1:
        if count2 > len(adj[i]):
            ans += count2 - len(adj[i])
            count1 -= 1
    else:
        if count1 > len(adj[i]):
            ans += count1 - len(adj[i])
            count2 -= 1
print(ans)
