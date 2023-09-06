from collections import deque

def solution(m, n, board):
    tmp = deque()
    board_stack = []
    count = 0

    for i in range(n):
        for j in range(m):
            tmp.append(board[j][i])
        board_stack.append(tmp)
        tmp = deque()


    while True:
        memo = []
        for r in range(n-1):
            for c in range(m-1):
                if board_stack[r][c] == '#':
                    continue
                if board_stack[r][c] == board_stack[r][c+1] == board_stack[r+1][c] == board_stack[r+1][c+1]:
                    memo.append((r, c))
        if not memo:
            break

        for r, c in memo:
            board_stack[r][c] = '@'
            board_stack[r][c+1] = '@'
            board_stack[r+1][c] = '@'
            board_stack[r+1][c+1] = '@'

        for stack in board_stack:
            while '@' in stack:
                stack.remove('@')
                stack.appendleft('#')
                count += 1
            print(stack)

    return count
