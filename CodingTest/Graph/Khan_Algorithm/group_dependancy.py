from collections import deque

class Solution:
    def topology_sort(self, graph, indegree, n):
        result = []
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            cur_v = q.popleft()
            result.append(cur_v)

            for target_v in graph[cur_v]:
                indegree[target_v] -= 1
                if indegree[target_v] == 0:
                    q.append(target_v)
        
        for i in indegree:
            if i != 0:
                return False
        return True

    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * (numCourses)
        graph = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        answer = self.topology_sort(graph, indegree, numCourses)

        return answer