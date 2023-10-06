# 파괴되지 않은 건물
# url - https://school.programmers.co.kr/learn/courses/30/lessons/92344

#성공 코드
def solution(board, skill):
    row = len(board)
    col = len(board[0])
    sum_board = [[0] * col for _ in range(row)]
    answer = 0

    for types, r1, c1, r2, c2, degree in skill:
        if types == 1:
            sum_board[r1][c1] += degree * (-1)
            if (r2 + 1) <= row - 1:
                sum_board[r2+1][c1] += degree
            if (c2 + 1) <= col - 1:
                sum_board[r1][c2+1] += degree
            if (r2 + 1) <= row - 1 and (c2 + 1) <= col - 1:
                sum_board[r2+1][c2+1] += degree * (-1)
        else:
            sum_board[r1][c1] += degree
            if (r2 + 1) <= row - 1:
                sum_board[r2+1][c1] += degree * (-1)
            if (c2 + 1) <= col - 1:
                sum_board[r1][c2+1] += degree * (-1)
            if (r2 + 1) <= row - 1 and (c2 + 1) <= col - 1:
                sum_board[r2+1][c2+1] += degree

    
    for row in range(len(sum_board)):
        for col in range(len(sum_board[0])):
            if col >= 1:
                sum_board[row][col] += sum_board[row][col-1]
    
    for col in range(len(sum_board[0])):
        for row in range(len(sum_board)):
            if row == 0:
                if board[row][col] + sum_board[row][col] > 0:
                    answer += 1
            else:
                sum_board[row][col] += sum_board[row-1][col]
                if board[row][col] + sum_board[row][col] > 0:
                    answer += 1

    return answer

    
"""
#실패 코드
def solution(board, skill):
    row = len(board)
    col = len(board[0])
    sum_board = [[0] * col for _ in range(row)]
    answer = 0

    for types, r1, c1, r2, c2, degree in skill:
        if types == 1:
            while r1 <= r2:
                sum_board[r1][c1] += degree * (-1)
                if (c2 + 1) <= col - 1:
                    sum_board[r1][c2+1] += degree
                r1 += 1
        else:
            while r1 <= r2:
                sum_board[r1][c1] += degree
                if (c2 + 1) <= col - 1:
                    sum_board[r1][c2+1] += degree * (-1)
                r1 += 1

    
    for row in range(len(sum_board)):
        for col in range(len(sum_board[0])):
            if col >= 1:
                sum_board[row][col] += sum_board[row][col-1]
            #board[row][col] += sum_board[row][col]
            if board[row][col] + sum_board[row][col] > 0:
                answer += 1
"""

"""
1. 성공 알고리즘 - 누적합
심화 - 2차원의 누적합
[원리]
skill 이 [2, 1, 0, 2, 2, 2] 로 주어졌다고 가정하자. 그러면
type = 2, r1 = 1, c1 = 0, r2 = 2, c2 = 2, degree = 2 가 된다.
이 때, (r2 + 1, c1), (r1, c2 + 1), (r2 + 1, c2 + 1)에 각각 degree * (-1), degree * (-1), degree 를 찍는다.
이렇게 하는 이유는 우리가 순회를 우측으로 한줄씩하고, 가로 장벽을 만들면 세로 순회를 한줄씩 하기 위해서이다. 순서를 살펴보면,
#1 점 찍기
[0, 0, 0, 0, 0]
[2, 0, 0, -2, 0]
[0, 0, 0, 0, 0]
[-2, 0, 0, 2, 0]
#2 가로 순회 한줄씩
[ 0,  0,  0, 0, 0]
[ 2,  2,  2, 0, 0]
[ 0,  0,  0, 0, 0]
[-2, -2, -2, 0, 0]
#3 세로순회 한줄씩
[0, 0, 0, 0, 0]
[2, 2, 2, 0, 0]
[2, 2, 2, 0, 0]
[0, 0, 0, 0, 0]

입출력 예1
#1
[-4, -1, 0, 0, 1]
[2, 0, -2, 0, 0]
[-2, 0, 0, 0, 2]
[2, 0, 0, 0, -2]
#2
[-4, -5, -5, -5, -4]
[ 2, 2, 0, 0, 0]
[-2, -2, -2, -2, 0]
[ 2, 2, 2, 2, 0]
#3
[-4, -5, -5, -5, -4]
[-2, -3, -5, -5, -4]
[-4, -5, -7, -7, -4]
[-2, -3, -5, -5, -4]

이렇게 하면 시간복잡도는 M x N = n, 3 * len(skills) = a 이라 했을 때, a + 2n 이 된다.
M x N 의 최대는 10^6 이고, a 의 최대는 250,000 * 3 이므로 O(a) < O(M x N) 이다.
따라서, big-O 는 O(n)이 된다.
"""

"""
첫 실패 사유
skill 이 [2, 1, 0, 2, 2, 2] 로 주어졌다고 가정하자. 그러면
type = 2, r1 = 1, c1 = 0, r2 = 2, c2 = 2, degree = 2 가 된다.
처음에는,
[0, 0, 0, 0, 0]
[2, 0, 0, -2, 0]
[2, 0, 0, -2, 0]
[0, 0, 0,  0, 0]
과 같이 type == 2이기 때문에
while r1 <= r2:
    (r1, c2 + 1) 위치에 degree * (-1)
    r1 += 1
을 해놓는다.
그리고 우측으로 누적합을 하며 한줄씩 진행한다.

시간초과가 났던 이유는 skill case 한번 당 세로로 -2의 점을 찍는 횟수가 r2 - r1이라는 점이다. 이렇게 되면 세로로 길쭉한 사각형에 skill이 n회 반복되면, (r2 - r1) * n 회의 시간복잡도가 걸리게 되는데, r2 -r1이 클 경우 이는 큰 시간복잡도를 잡아먹을 수 있다. 

물론, 경우에 따라 가로로 길쭉한 사각형일 경우에는 오히려 더 짧은 시간복잡도가 걸릴 수 있다. 하지만 big - O 가 위와 같은 원리에 의해 일반적인 경우에서 또한 문제가 생길 수 있다.
"""