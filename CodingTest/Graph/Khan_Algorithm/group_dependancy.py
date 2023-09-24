from collections import deque

class Solution:
    def inside_group_topology_sort(self, graph, indegree, search_group):
        #@print("현재 파악중인 그룹아이템들:", search_group, indegree)
        result = []
        q = deque()

        for item in search_group:
            if indegree[item] == 0:
                q.append(item)
        
        while q:
            prev_v = q.popleft()
            result.append(prev_v)

            for next_v in graph[prev_v]:
                indegree[next_v] -= 1
                if indegree[next_v] == 0:
                    q.append(next_v)
        #@print("위상정렬 결과:", result)

        if len(result) != len(search_group):
            return False

        return result

    def graph_topology_sort(self, group, beforeItems, m):
        # group : [-1,-1,1,0,0,1,0,-1]
        # group_by_result : [[6, 3, 4], [5, 2], [0], [1], [7]]
        # beforeItems : [[],[6],[5],[6],[3,6],[],[],[]]
        count = m
        for i in range(len(group)): # -1 그룹을 각각 m, m+1, ... 의 개별 그룹으로 변경
            if group[i] == -1:
                group[i] = m
                m += 1
        #@print("현재 그룹 정보", group) # [2, 3, 1, 0, 0, 1, 0, 4]
        
        graph = [[] for i in range(m)]
        indegree = [0] * m
        # graph = [[], [], [], [], []]
        for next_v, prev_list in enumerate(beforeItems):
           for prev_v in prev_list:
               if group[next_v] != group[prev_v]: #  group[prev_v or next_v] : 변경된 아이템 그룹
                   graph[group[prev_v]].append(group[next_v])
                   indegree[group[next_v]] += 1
        
        print("수정된 그룹 정보:", group, "깊이:", indegree)
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
        print("그룹간의 위상정렬 결과:", result)

        if len(result) != len(graph):
            return False

        return result

        
        
        #@print("최종 답 예상:", answer)

        return answer

    def sortItems(self, n, m, group, beforeItems):
        group_by_result = []
        items_by_group = [[] for i in range(m+1)]
        for item, group_num in enumerate(group):
            items_by_group[group_num+1].append(item)
        groups_by_group = [[] for i in range(m)]
        for i in range(len(items_by_group[0])):
            groups_by_group.append([])
        print("groups_by_group", groups_by_group)
        sorted_graph = self.graph_topology_sort(group, beforeItems, m)
        print(sorted_graph)
        if sorted_graph == False:
            return []

        print("그룹별 정리된 아이템들:", items_by_group)

        for group_num in range(m):  # m: 문제에서 주어진 m번째 그룹
            result = []
            graph = [[] for i in range(n)]
            indegree = [0] * n
            for next_v, prev_li in enumerate(beforeItems): # next_v: 1 prev_li : 0 1 4
                if group[next_v] == group_num:
                    #@print("next_v:", next_v, "is same with group num:", group_num)
                    for prev_v in prev_li:
                        if group[prev_v] == group_num:
                            graph[prev_v].append(next_v)
                            indegree[next_v] += 1
                        

            #@print("graph:", graph, "그룹 번호:", group_num, "깊이:", indegree)
            # m이 0(그룹)이면, graph = [[], [], [], [4], [], [], [3, 4], []]일 것이다.
            result = self.inside_group_topology_sort(graph, indegree, items_by_group[group_num+1])
            if result == False:
                return []
            group_by_result.append(result)
        for special_item in items_by_group[0]:
            group_by_result.append([special_item])
        
        print("최종 그루핑:", group_by_result)
        answer = []
        for i in sorted_graph:
            for val in group_by_result[i]:
                answer.append(val)
        return answer
