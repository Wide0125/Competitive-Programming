import sys

N, M = map(int, input().split())
adj = [[] for _ in range(M)]
for a in range(N):
    c1, c2 = map(int, input().split())
    adj[c1 - 1].append((c2 - 1, a))
    adj[c2 - 1].append((c1 - 1, a))


visited = [False] * M
rejected = []
for i in range(M):
    if visited[i]:
        continue
    curr_visited = [False] * M
    todo = [(i, None, None)]
    extras = []
    parent = None
    while todo:
        curr, cow, curr_parent = todo.pop()
        if not visited[curr] and not curr_visited[curr]:
            visited[curr] = True
            curr_visited[curr] = True
            for j in adj[curr]:
                todo.append(j + tuple([parent]))
        elif curr_visited and curr != curr_parent:
            extras.append(curr)
            rejected.append(cow)
        parent = curr
for a in rejected:
    print(a + 1)
