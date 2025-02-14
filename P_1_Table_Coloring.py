n, m, k = map(int, input().split())
table = [[-1] * m for _ in range(n)]
colored_cells = []
for i in range(k):
    x, y, c = map(int, input().split())
    table[y - 1][x - 1] = c
    colored_cells.append([x - 1, y - 1])
    
print(not (False ^ True ^ True))
