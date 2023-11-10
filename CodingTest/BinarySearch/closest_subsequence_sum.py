# https://leetcode.com/problems/closest-subsequence-sum/

import bisect

class Solution:
    def minAbsDifference(self, nums, goal: int):
        def make_subset(nums):
            ans = {0}
            for num in nums:
                ans |= {num + i for i in ans}
            return ans

        first = make_subset(nums[:len(nums)//2])
        second = make_subset(nums[len(nums)//2:])

        first = sorted(first)
        ans = inf

        for i in second:
            diff = goal - i
            k = bisect_left(first, diff)
            if k < len(first):
                ans = min(ans, first[k] + i - goal)
            if  0 < k:
                ans = min(ans, goal - i - first[k-1])
        
        return ans

"""
[핵심 알고리즘] : binary search + binary search의 최적화

python의 bisect 이용! bisect_left(리스트, goal)은 리스트에서 binary search를 진행했을 때, goal이 존재하면 가장 좌측의 인덱스를, 존재하지 않으면 어떤 인덱스에 들어가야 하는지(좌측)를 알려준다.

nums리스트를 통째로 binary search를 진행하면, n개 요소에 대해 부분합을 만들고 시작하는데, 이 시간도 길 뿐더러 이 상태에서 binary search를 진행하는 속도 또한 느리다. n이 클수록 부분합을 만드는 과정의 big-O는 nC0+nC1+…nCn 가 되어 분자가 기하급수적으로 커지기 때문이다. (big-O를 따진 것이고, 분자에 n!의 요소가 포함되기 때문. 세부 구현을 어떻게 하든 위의 최악의 상황은 모든 부분합의 원소가 다른 경우이기 때문)

이를 막기 위해, 
1. n/2개수로 nums리스트를 반반 쪼개고 각각 부분합의 집합을 만든다. 
2. 한쪽 부분합 집합의 요소 갯수만큼 반복하며, 각 반복마다 binary search를 진행해서 시간복잡도를 줄인다.
(세부적으로는 한쪽 부분합 집합의 요소 갯수만큼 반복하며를 할 때, 나머지 부분합 집합을 정렬시킨 결과값을 리스트로 변환시키고 이 리스트에서 binary search를 진행하게 한다. 이 때의 목표값은 (기존 목표 - 첫번째 집합의 요소의 값)이 된다.
이렇게하면, n이 절반으로 주는데 발생하는 이득이 부분합 집합 한쪽 원소의 수만큼 반복하며 절반 길이의 nums리스트로 만들어진 부분합의 집합에서 goal을 찾는 binary search를 반복하는 상황이 발생하는데, 이게 훨신 더 시간복잡도 측면해서 유리하다.
"""