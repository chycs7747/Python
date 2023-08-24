# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque

def sum_same(queue1, queue2):
    ans = -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    target_sum = (queue1_sum + queue2_sum) / 2
    check_input_total_odd = (queue1_sum + queue2_sum) % 2

    if check_input_total_odd == 1:
        return ans

    for i in range(len(queue1)*4):
        if target_sum < queue1_sum:
            data = queue1.popleft()
            queue2.append(data)
            queue1_sum -= data
            queue2_sum += data
        elif target_sum < queue2_sum:
            data = queue2.popleft()
            queue1.append(data)
            queue2_sum -= data
            queue1_sum += data
        elif target_sum == queue1_sum and target_sum == queue2_sum:
            ans = i
            break

    return ans


print(sum_same(queue1=[1, 1, 1, 8, 10, 9], queue2=[1, 1, 1, 1, 1, 1]))
