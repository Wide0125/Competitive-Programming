import sys
input = sys.stdin.readline

# TLE on cases 7 and 10
def test_win(board):  # checks for winning board
    new_board = [[0] * 3 for _ in range(3)]
    for k in range(3):
        for l in range(3):
            new_board[k][l] = board[(k * 3) + l]
    for r in range(3):
        if new_board[r][0] == 3 and new_board[r][1] == 2 and new_board[r][2] == 2:
            return True
        elif new_board[r][0] == 2 and new_board[r][1] == 2 and new_board[r][2] == 3:
            return True
    for c in range(3):
        if new_board[0][c] == 3 and new_board[1][c] == 2 and new_board[2][c] == 2:
            return True
        if new_board[0][c] == 2 and new_board[1][c] == 2 and new_board[2][c] == 3:
            return True
    if new_board[0][0] == 3 and new_board[1][1] == 2 and new_board[2][2] == 2:
        return True
    if new_board[0][0] == 2 and new_board[1][1] == 2 and new_board[2][2] == 3:
        return True
    if new_board[0][2] == 3 and new_board[1][1] == 2 and new_board[2][0] == 2:
        return True
    if new_board[0][2] == 2 and new_board[1][1] == 2 and new_board[2][0] == 3:
        return True
    return False


N = int(input())
maze = []
for a in range(N):  # populating maze list while simultaneously getting starting position
    small_curr = input()
    temp = []
    for b in range(N):
        curr2 = small_curr[3 * b: 3 * b + 3]
        if curr2 == 'BBB':
            start_pos = [a, b, [1] * 9]
            curr2 = '...'
        temp.append(curr2)
    maze.append(temp)
todo = [start_pos]
cycle = [[0, 1], [0, -1], [1, 1], [1, -1]]
visited = [[[False] * (3 ** 9) for _ in range(25)] for _ in range(25)]
wins = [False] * (3 ** 9)
ans = 0
while todo:  # DFS
    curr = todo.pop()
    a = curr[0]
    b = curr[1]
    if maze[a][b] == '###':
        continue
    board = curr[2]
    if maze[a][b] != '...':
        move = maze[a][b]
        i, j = int(move[1]) - 1, int(move[2]) - 1
        if board[i * 3 + j] == 1:
            if move[0] == 'O':
                board[i * 3 + j] = 2
            else:
                board[i * 3 + j] = 3
    b_index = 0
    for _ in range(8, -1, -1):
        b_index += (int(board[_]) - 1) * 3 ** (8 - _)
    if not visited[a][b][b_index]:
        visited[a][b][b_index] = True
        if not wins[b_index]:
            if test_win(board):
                ans += 1
                wins[b_index] = True
                continue
        else:
            continue  # stops movement once winning board is reached
        for i in range(4):
            a = curr[0]
            b = curr[1]
            if cycle[i][0] == 0:
                a += cycle[i][1]
            else:
                b += cycle[i][1]
            todo.append([a, b, board.copy()])
print(ans)
string = "suicide"
