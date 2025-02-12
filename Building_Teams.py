import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friendships = [list(map(int, input().split())) for _ in range(m)]
adj = [[] for _ in range(n)]
for i in friendships:
    a = i[0] - 1
    b = i[1] - 1
    adj[a].append(b)
    adj[b].append(a)
    
teams = [0] * n
todo = []
for i in range(n):
    if teams[i]:
        continue
    todo.append(i)
    teams[i] = 1
    while todo:
        curr = todo.pop()
        for next in adj[curr]:
            if teams[next]:
                if teams[next] == teams[curr]:
                    print("IMPOSSIBLE")
                    exit()
            else:
                teams[next] = 2 if teams[curr] == 1 else 1
                todo.append(next)
print(*teams)
    