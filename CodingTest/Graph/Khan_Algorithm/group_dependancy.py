from collections import deque

class Solution:
    def item_topology_sort(self, graph, indegree):
        result = []
        q = deque()
        for i, item in enumerate(indegree):
            if item == 0:
                q.append(i)
        while q:
            prev_v = q.popleft()
            result.append(prev_v)

            for next_v in graph[prev_v]:
                indegree[next_v] -= 1
                if indegree[next_v] == 0:
                    q.append(next_v)

        for i in indegree:
            if i != 0:
                return False
        return result


    def graph_topology_sort(self, group, beforeItems, m):
        graph = [[] for i in range(m)]
        indegree = [0] * m
        for next_v, prev_list in enumerate(beforeItems):
           for prev_v in prev_list:
               if group[next_v] != group[prev_v]: #  group[prev_v or next_v] : 변경된 아이템 그룹
                   graph[group[prev_v]].append(group[next_v])
                   indegree[group[next_v]] += 1
      
        result = []
        q = deque()
        for i in range(len(graph)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            prev_v = q.popleft()
            result.append(prev_v)

            for next_v in graph[prev_v]:
                indegree[next_v] -= 1
                if indegree[next_v] == 0:
                    q.append(next_v)

        if len(result) != len(graph):
            return False
        return result

    def sortItems(self, n: int, m: int, group, beforeItems):
        #data reconstruct
        for i in range(len(group)): # -1 그룹을 각각 m, m+1, ... 의 개별 그룹으로 변경
            if group[i] == -1:
                group[i] = m
                m += 1
        #topology sort by groups
        sorted_group = self.graph_topology_sort(group, beforeItems, m)
        if sorted_group == False:
            return []
				
        #topology sort by items
        indegree = [0] * (n)
        graph = [[] for i in range(n)]
        for next_v, prev_list in enumerate(beforeItems):
            for prev_v in prev_list:
                graph[prev_v].append(next_v)
                indegree[next_v] += 1
        sorted_item = self.item_topology_sort(graph, indegree)
        if sorted_item == False:
            return []

        result = [[] for i in range(m)]
        answer = []
        for cur_v in sorted_item:
            result[group[cur_v]].append(cur_v)
        for group_num in sorted_group:
            for item in result[group_num]:
                answer.append(item)
        
        return answer