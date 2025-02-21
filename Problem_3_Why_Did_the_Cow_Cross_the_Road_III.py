N, K, R = map(int, input().split())
roads = [[[] for _ in range(N)] for _ in range(N)]
for i in range(R):
    i1, j1, i2, j2 = map(int, input().split())

cows = [tuple(map(int, input().split())) for _ in range(K)]

