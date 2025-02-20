import sys, os.path
if(os.path.exists('perimeter.in')):
    sys.stdin = open("perimeter.in", "r")
    sys.stdout = open("perimeter.out", "w")

N = int(input())
grid = [list(input()) for _ in range(N)]
grid.append(['.'] * N)
visited = [[False] * N for _ in range(N)]
visited.append(['.'] * N)
for i in range(N):
    grid[i].append('.')
    visited[i].append('.')

directions = [1, -1]
area_min = 0
peri_min = float('inf')
for i in range(N):
    for j in range(N):
        if visited[i][j] or grid[i][j] == '.':
            continue
        todo = [(i, j)]
        area = 0
        perimeter = 0
        while todo:
            a, b = todo.pop()
            if visited[a][b]:
                continue
            visited[a][b] = True
            area += 1
            for k in directions:
                if grid[a + k][b] == '.':
                    perimeter += 1
                else:
                    todo.append((a + k, b))
                if grid[a][b + k] == '.':
                    perimeter += 1
                else:
                    todo.append((a, b + k))
        if area > area_min:
            area_min = area
            peri_min = perimeter
        elif area == area_min:
            peri_min = min(peri_min, perimeter)
print(f"{area_min} {peri_min}")
