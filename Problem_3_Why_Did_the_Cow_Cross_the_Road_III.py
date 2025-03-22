import sys, os.path
if(os.path.exists("countcross.in")):
    sys.stdin = open("countcross.in", "r")
    sys.stdout = open("countcross.out", "w")


N, K, R = map(int, input().split())
roads = [[[] for _ in range(N)] for _ in range(N)]
for i in range(R):
    i1, j1, i2, j2 = map(int, input().split())
    roads[i1 - 1][j1 - 1].append((i2 - 1, j2 - 1))
    roads[i2 - 1][j2 - 1].append((i1 - 1, j1 - 1))    
grid = [[0] * N for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    grid[a - 1][b - 1] = 1
grid.append([-1] * N)
visited = [[False] * N for _ in range(N)]
visited.append([True] * N)
for i in range(N):
    grid[i].append(-1)
    visited[i].append(True)

connected_cows = []
for i in range(N):
    for j in range(N):
        if grid[i][j] != 1 or visited[i][j]:
            continue
        cow_count = 0
        todo = [(i, j)]
        while todo:
            a, b = todo.pop()
            if visited[a][b] or grid[a][b] == -1:
                continue
            visited[a][b] = True
            if grid[a][b] == 1:
                cow_count += 1
            if (a + 1, b) not in roads[a][b]:
                todo.append((a + 1, b))
            if (a - 1, b) not in roads[a][b]:
                todo.append((a - 1, b))
            if (a, b + 1) not in roads[a][b]:
                todo.append((a, b + 1))
            if (a, b - 1) not in roads[a][b]:
                todo.append((a, b - 1))
        connected_cows.append(cow_count)
ans = 0
for i in range(len(connected_cows)):
    for j in range(i + 1, len(connected_cows)):
        ans += connected_cows[i] * connected_cows[j]
print(ans)
