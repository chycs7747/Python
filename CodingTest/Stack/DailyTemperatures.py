"""
매일의 온도를 나타내는 int형 배열 temperatures가 주어진다. answer배열의 원소 answer[i]는 i번 째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다.
만약 더 따뜻해지는 날이 없다면 answer[i] == 0 이다. answer 배열을 반환하는 함수를 구현하시오.

제약조건
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

input : temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
output : [1, 1, 4, 2, 1, 1, 0, 0]

input : temperatures = [30, 40, 50, 60]
output : [1, 1, 1, 0]

input : temperatures = [30, 60, 90]
output : [1, 1, 0]
"""

"""
완전탐색 -> n^2 ->(10^5)^2 = 10^10 -> 시간 초과
"""

def dailyTemperatures(temperatures):
    output = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        if not stack or (stack[-1][1] > cur_temp):
            stack.append((cur_day, cur_temp))
        else:
            while stack and (stack[-1][1] < cur_temp):              
                prev_day = stack.pop()[0]
                output[prev_day] = cur_day - prev_day
            stack.append((cur_day, cur_temp))
    return output

#print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

"""
def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
"""