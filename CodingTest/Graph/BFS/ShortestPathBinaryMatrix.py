"""
문제 url
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""
from collections import deque

grid1 = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0]
]
grid2 = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]


def shortest_path(grid):
    if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] == 1:
        return -1
    d_col = [-1, 0, 1, 1, 1, 0, -1, -1]
    d_row = [1, 1, 1, 0, -1, -1, -1, 0]
    visited = [(0, 0, 1)]
    queue = deque()
    queue.append((0, 0, 1))
    flag = 0
    while queue:
        cur_row, cur_col, cur_length = queue.popleft()
        for idx in range(8):
            nxt_row, nxt_col, nxt_length = cur_row + d_row[idx], \
                    cur_col + d_col[idx], cur_length+1
            if 0 <= nxt_row < len(grid) and 0 <= nxt_col < len(grid[0]) \
                    and grid[nxt_row][nxt_col] == 0:
                for element in visited:
                    if (nxt_row, nxt_col) == (element[0], element[1]):
                        flag = 1
                        if nxt_length < element[2]:
                            queue.append((nxt_row, nxt_col, nxt_length))
                            visited.append((nxt_row, nxt_col, nxt_length))
                if flag == 0:
                    queue.append((nxt_row, nxt_col, nxt_length))
                    visited.append((nxt_row, nxt_col, nxt_length))
                flag = 0

    return visited


path = shortest_path(grid1)


def ans(grid):
    if path == -1:
        print(-1)
    else:
        li = []
        for element in path:
            if element[0] == len(grid)-1 and element[1] == len(grid[0])-1:
                li.append(element[2])
        if li:
            print(min(li))
        else:
            print(-1)


ans(grid1)
