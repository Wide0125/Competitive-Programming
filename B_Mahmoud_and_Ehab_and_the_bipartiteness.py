n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
adj = [[] for _ in range(n)]
for i in edges:
    a = i[0] - 1
    b = i[1] - 1
    adj[a].append(b)
    adj[b].append(a)
teams = [0] * n

todo = [0]
teams[0] = 1
count1 = 1
count2 = 0
while todo:
    curr = todo.pop()
    for next in adj[curr]:
        if not teams[next]:
            if teams[curr] == 1:
                teams[next] = 2
                count2 += 1
            else:
                teams[next] = 1
                count1 += 1
            todo.append(next)
print(count1 * count2 - (n - 1))
