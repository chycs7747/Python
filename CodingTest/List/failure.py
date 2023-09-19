from collections import deque
import heapq


"""
def solution(N, stages):
    answer = []
    memo = []
    
    n = len(stages)

    for i in range(N):
        if n == 0:
            memo.append((0, i+1))
        num = stages.count(i+1)
        p = round(num/n, 4)
        memo.append((-p, i+1))
        n -= num
    
    print("start")
    for x,y in memo:
        print(x, y)
    print("end")
    
    print("restart")
    print(memo)
    heapq.heapify(memo)
#    memo = [(-x,y) for (x,y) in memo]
    print(memo)
    print("reend")

    while memo:
        value = heapq.heappop(memo)
        answer.append(value[1])
    
    return answer
"""


def solution(N, stages):
    answer = []
    memo = []
    n = len(stages)

    for i in range(N):
        if n == 0:
            memo.append((0, i+1))
            continue
        num = stages.count(i+1)
        p = num/n
        memo.append((p, i+1))
        n -= num
    
    memo.sort(reverse=True)

    prev_p = memo[0][0]
    start_i = 0
    
    tmp = []
    for i in range(N):
        if prev_p == memo[i][0]:
            if i == N-1:
                tmp.append(memo[i])
                tmp.sort()
                memo[start_i:] = tmp
            else:
                tmp.append(memo[i])
        else:
            tmp.sort()
            memo[start_i:i] = tmp
            start_i = i
            prev_p = memo[start_i][0]
            tmp = [memo[start_i]]

    for val in memo:
        answer.append(val[1])

    return answer

answer = solution(5, [3, 2, 1, 1])
print(answer)