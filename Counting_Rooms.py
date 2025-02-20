n, m = map(int, input().split())
map = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

rooms = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] or map[i][j] == '#':
            continue
        todo = [[i, j]]
        while todo:
            a, b = todo.pop()
            if visited[a][b] or map[a][b] == '#':
                continue
            visited[a][b] = True
            if a < n - 1:
                todo.append([a + 1, b])
            if a > 0:
                todo.append([a - 1, b])
            if b < m - 1:
                todo.append([a, b + 1])
            if b > 0:
                todo.append([a, b - 1])
        rooms += 1
print(rooms)
            