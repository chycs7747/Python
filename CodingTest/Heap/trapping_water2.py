# https://leetcode.com/problems/trapping-rain-water-ii/description/

import heapq

class Solution:
    def trapRainWater(self, heightMap):
        answer = 0
        min_heap = [] # min-heap
        map_row = len(heightMap)
        map_col = len(heightMap[0])

        # heap data processing
        for row in range(map_row):
            for col in range(map_col):
                if row == 0 or row == map_row - 1:
                    min_heap.append((heightMap[row][col], (row, col)))
                else:
                    if col == 0 or col == map_col - 1:
                        min_heap.append((heightMap[row][col], (row, col)))

        heapq.heapify(min_heap)
        visited = [[False]*map_col for _ in range(map_row)]
        check_height = min_heap[0][0]
        d_row = [0, 0, 1, -1]
        d_col = [1, -1, 0, 0]
    

        while min_heap:
            if min_heap[0][0] == check_height:
                cur_row, cur_col = heapq.heappop(min_heap)[1]
                visited[cur_row][cur_col] = True

                for i in range(4):
                    next_row = cur_row + d_row[i]
                    next_col = cur_col + d_col[i]
                    
                    if (0 <= next_col <= map_col - 1)  and (0 <= next_row <= map_row - 1) and not visited[next_row][next_col]:
                        if heightMap[next_row][next_col] < check_height:
                            answer += (check_height - heightMap[next_row][next_col])
                            heightMap[next_row][next_col] = check_height
                        visited[next_row][next_col] = True
                        heapq.heappush(min_heap, (heightMap[next_row][next_col], (next_row, next_col)))
            if min_heap:
                check_height = min_heap[0][0]

        return answer
