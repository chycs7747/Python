# https://school.programmers.co.kr/learn/courses/30/lessons/42586/

"""
입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

제한조건
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
"""


def function_develop(progresses, speeds):
    complete_date = []
    stack = []
    ans = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i]:
            complete_date.append(((100 - progresses[i]) // speeds[i]) + 1)
        else:
            complete_date.append(((100 - progresses[i]) // speeds[i]))
    for cur_date in complete_date:
        if not stack or stack[0] >= cur_date:
            stack.append(cur_date)
        else:
            ans.append(len(stack))
            stack.clear()
            stack.append(cur_date)
    if stack:
        ans.append(len(stack))
    return ans


print(function_develop(progresses = [93,30,55], speeds = [1,30,5]))

"""
DailyTemperature 문제 응용이라 판단하고 진행
"""