from collections import deque


def solution(board, moves):
    ans = []
    answer = 0
    tmp = deque()
    board_queue = deque()
    board_length = len(board)

    for i in range(board_length):
        for j in range(board_length):
            if board[j][i] != 0:
                tmp.append(board[j][i])
        board_queue.append(tmp)
        tmp = deque()
    for move in moves:
        if not board_queue[move-1]:
            continue
        data = board_queue[move-1].popleft()
        board_queue.append(0)
        if ans and (ans[-1] == data):
            ans.pop()
            answer += 2
        else:
            ans.append(data)
    return answer


result = solution(
    board=[[0, 0, 0, 0, 0],
           [0, 0, 1, 0, 3],
           [0, 2, 5, 0, 1],
           [4, 2, 4, 4, 2],
           [3, 5, 1, 3, 1]],
    moves=[1, 5, 3, 5, 1, 2, 1, 4])
print(result)
