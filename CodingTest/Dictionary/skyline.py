# uri : https://leetcode.com/problems/the-skyline-problem/description/
class Solution:
    def getSkyline(self, buildings):
        answer = []
        prev_height = 0
        points_set = set()
        points = {}
        for x, y, h in buildings:
            points_set.add(x)
            points_set.add(y)
        points_set = sorted(points_set)

        for point in points_set:
            points[point] = 0

        for point in points.keys():
            for building in buildings:
                if building[0] <= point < building[1]:
                    if points[point] < building[2]:
                        points[point] = building[2]

        for left, height in points.items():
            if prev_height != height:
                prev_height = height
                answer.append([left, height])

        return answer

"""
building의 수 ≤ 10^4 즉, n^2까지 이용가능

1. 따라서, 각 building left, right 점을 미리 오름차순 정렬을 시켜두고
→ points =  {point: height(default=0)},
2. 각 점을 순회하며,
해당 점이 building left ≤ point < building right 일 때,
해당 점의 높이를 계속 최고 높이로 update시킨다. (같은 점에 대해 여러 height이 존재하기 때문)
→ points[point] = maximum height update
3. 최종적으로, points의 각 점(오름차순으로 정렬된)을 순회하며 현재 점의 height가 직전 점의 height와 같은 높이가
아닐 경우에만 Output(answer)에 [left, height]의 쌍으로 append한다.
"""