import sys, os.path
if(os.path.exists('multimoo.in')):
    sys.stdin = open("multimoo.in", "r")
    sys.stdout = open("multimoo.out", "w")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


def size(i, j, og_id):
    global visited
    todo = [(i, j)]
    id = grid[i][j]
    ret = 0
    while todo:
        a, b = todo.pop()
        try:
            if a < 0 or a > N - 1 or b < 0 or b > N - 1:
                continue
            if (grid[a][b] == id or grid[a][b] == og_id) and not visited[a][b]:
                visited[a][b] = True 
                ret += 1
                todo.append((a + 1, b))
                todo.append((a - 1, b))
                todo.append((a, b + 1))
                todo.append((a, b - 1))
        except IndexError:
            continue
    return ret


pointer = -1
solo_max = 0
team_max = 0
areas = []
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        todo = [(i, j)]
        id = grid[i][j]
        adjacent_sizes = [0] * int(1e6)
        pointer += 1
        curr_pointer = pointer
        adjacent_coords = []
        areas.append(0)
        while todo:
            a, b = todo.pop()
            if a < 0 or a > N - 1 or b < 0 or b > N - 1:
                continue
            if grid[a][b] == id and not visited[a][b]:
                visited[a][b] = True
                areas[curr_pointer] += 1
                todo.append((a + 1, b))
                todo.append((a - 1, b))
                todo.append((a, b + 1))
                todo.append((a, b - 1))
            elif not visited[a][b]:
                adjacent_coords.append((a, b))
        for a2, b2 in adjacent_coords:
            if not visited[a2][b2]:
                adjacent_sizes[grid[a2][b2]] += size(a2, b2, id)
            else:
                adjacent_sizes[grid[a2][b2]] += 
        solo_max = max(solo_max, curr_solo)
        team_max = max(team_max, curr_solo + max(adjacent_sizes))
print(solo_max)
print(team_max)
