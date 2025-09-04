import sys
sys.stdin = open("shell.in", 'r')
sys.stdout = open("shell.out", 'w')

N = int(input())
turns = []
for n in range(N):
    turns.append(list(map(int, input().split())))

score = 0
for i in range(3):
    currScore = 0
    pebble = i + 1
    for j in range(N):
        change1 = turns[j][0]
        change2 = turns[j][1]
        if pebble == change1:
            pebble = change2
        elif pebble == change2:
            pebble = change1
        chose = turns[j][2]
        if chose == pebble:
            currScore += 1
    score = max(currScore, score)

print(score)
        
       
