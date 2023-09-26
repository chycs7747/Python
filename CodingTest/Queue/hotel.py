# https://school.programmers.co.kr/learn/courses/30/lessons/155651

import heapq

def solution(book_time):
    for i, times in enumerate(book_time):
        for j, time in enumerate(times):
            if j == 0:
                book_time[i][j] = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
            else:
                book_time[i][j] = int(time.split(':')[0]) * 60 + int(time.split(':')[1]) + 10
    
    book_time.sort(reverse=True)
    heap = []
    end_point = book_time.pop()[1]
    heapq.heappush(heap, end_point)
    for i in range(len(book_time)):
        start_t, end_t = book_time.pop()
        if start_t >= end_point:    
            value = heapq.heappop(heap) # value for test
        if end_t <= end_point:
            end_point = end_t
        heapq.heappush(heap, end_t)
        end_point = heap[0]
    
    answer = len(heap)
    return answer