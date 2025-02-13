import sys, os
if(os.path.exists('revegetate.in')):
    sys.stdin = open('revegetate.in', 'r')
    sys.stdout = open("revegetate.out", 'w')
    
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for a in range(M):
    SD, p1, p2 = input().split()
    p1 = int(p1) - 1
    p2 = int(p2) - 1
    adj[p1].append([SD, p2])
    adj[p2].append([SD, p1])

ans = 1 
teams = [0] * N
for i in range(N):
    if not teams[i]:
        teams[i] = 1
        todo = [i]
        while todo:
            curr = todo.pop()
            for next in adj[curr]:
                SD, j = next[0], next[1]
                if SD == 'S':
                    if not teams[j]:
                        teams[j] = teams[curr]
                        todo.append(j)
                    elif teams[j] != teams[curr]:
                        print(0)
                        exit()
                else:
                    if not teams[j]:
                        teams[j] = 1 if teams[curr] == 2 else 2
                        todo.append(j)
                    elif teams[j] == teams[curr]:
                        print(0)
                        exit()
        ans *= 2
print(bin(ans)[2:])
    