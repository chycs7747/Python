# https://www.acmicpc.net/problem/1697
from collections import deque

"""
N, K = list(map(int, input().split()))
visited = {}
answer = 0
count = 0
def dfs(N, K, count):
    #print(N)
    if N == K:
        if count == 0:
            visited[K] = 0
        #print("도착", count)
        return
    for i in range(3):
        if N-1 not in visited or count+1 < visited[N-1]:
            #print("N>K(N-1)")
            dfs(N-1, K, count+1)
            visited[N-1] = count+1
        if N < K:
            if N+1 not in visited or count+1 < visited[N+1]:
                #print("N<K(N+1)")
                dfs(N+1, K, count+1)
                visited[N+1] = count+1
            if N != 0 and (N*2 not in visited or count+1 < visited[N*2]):
                #print("N<K(N*2)")
                dfs(N*2, K, count+1)
                visited[N*2] = count+1
    return
#dfs(N, K, 0)
#print(visited[K])

# 1. 타고가다가 N==K가 되면, answer = min(answer, count)를 한다.
# 타고 갈때는 dfs(N+a, K, coun+1)을 넘겨준다.
# 6 = 1 , 2, 3, 6
# 7 = 1, 2, 3, 6, 7 / 1, 2, 4, 8, 7
"""


from collections import deque

N, K = list(map(int, input().split()))

def bfs(N, K):
    visited = {N: 0}
    graph = deque([N])
    if N == K:
        return 0
    while graph:
        N = graph.popleft()
        if N-1 >= 0 and N-1 not in visited:
            if N-1 == K:
                return visited[N] + 1
            graph.append(N-1)
            visited[N-1] = visited[N] + 1
        if N < K:
            if N+1 not in visited:
                if N+1 == K:
                    return visited[N] + 1
                graph.append(N+1)
                visited[N+1] = visited[N] + 1
            if N != 0 and N*2 not in visited:
                if N*2 == K:
                    return visited[N] + 1
                graph.append(N*2)
                visited[N*2] = visited[N] + 1

print(bfs(N, K))
