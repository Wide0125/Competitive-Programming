n, m = map(int, input().split())
map = [list(input()) for _ in range(n)]
map.append(['#'] * m)
visited = [[False] * m for _ in range(n)]
visited.append([False] * m)

for a in range(n):
    map[a].append('#')
    visited[a].append(False)

rooms = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] or map[i][j] == '#':
            continue
        todo = [(i, j)]
        while todo:
            a, b = todo.pop()
            try:
                if visited[a][b] or map[a][b] == '#':
                    continue
                visited[a][b] = True
                todo.append((a + 1, b))
                todo.append((a - 1, b))
                todo.append((a, b + 1))
                todo.append((a, b - 1))
            except IndexError:
                continue
        rooms += 1
print(rooms)
            