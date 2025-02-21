for _ in range(int(input())):
    n, m = map(int, input().split())
    good_people_count = 0
    grid = []
    for i in range(n):
        temp = list(input())
        good_people_count += temp.count("G")
        grid.append(temp)
    grid.append(['#'] * m)
    possible = True
    visited = [[False] * m for _ in range(n)]
    visited.append([True] * m)
    for i in range(n + 1):
        grid[i].append('#')
        visited[i].append(True)
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] or grid[i][j] != 'B':
                continue
            todo = [(i, j)]
            while todo:
                a, b = todo.pop()
                if grid[a][b] == '#':
                    continue
                elif grid[a][b] == '.':
                    grid[a][b] = '#'
                    continue
                elif grid[a][b] == 'G':
                    possible = False
                    break
                elif a == n and b == m:
                    possible = False
                    break
                elif visited[a][b]:
                    continue
                visited[a][b] = True
                todo.append((a + 1, b))
                todo.append((a - 1, b))
                todo.append((a, b + 1))
                todo.append((a, b - 1))
            if not possible:
                break
        if not possible:
            break
    if not possible:
        print("No")
        continue
    else:
        todo = [(n - 1, m - 1)]
        while todo:
            a, b = todo.pop()
            if visited[a][b] or grid[a][b] == "#":
                continue
            visited[a][b] = True
            if grid[a][b] == 'G':
                good_people_count -= 1
            todo.append((a + 1, b))
            todo.append((a - 1, b))
            todo.append((a, b + 1))
            todo.append((a, b - 1))
    if not good_people_count:
        print("Yes")
    else:
        print("No")
            