N = int(input())
words = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
adj_len = [0] * (N + 1)
for i in range(N):
    adj[i + 1].append(words[i])
    adj[words[i]].append(i + 1)
    adj_len[i + 1] += 1
    adj_len[words[i]] += 1

visited = [False] * (N + 1)
M = adj_len[1:].count(1)
unique = [None] * (N + 1)
bank = [int(input()) for _ in range(M)]
for i in bank:
    todo = [i]
    depth = 0
    temp = 0
    fork = False
    while todo:
        curr = todo.pop()
        if visited[curr]:
            continue
        depth += 1
        temp += 1
        if (adj_len[curr] >= 3 or (curr == 0 and adj_len[0] > 1)) and not fork:
            depth = 0
            adj_len[curr] -= 1
            fork = True
        if curr == 0:
            if depth == temp:
                print(0)
            else:
                print(depth + 1)
            break
        todo.append(min(adj[curr]))
