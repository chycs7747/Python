# https://leetcode.com/problems/validate-binary-search-tree/description/

class Solution:
    def dfs(self, root, low, high):
        if not root:
            return True
        if not (low < root.val < high):
            return False
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)    


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -inf, inf)

"""
준 TreeNode의 형태
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
형태가 고정되어있다.

[핵심 알고리즘] : Binary Search Tree, DFS / 범위 접근

BST의 예시 중 [5,4,6,null,null,3,7] 에 대한 설명이 제대로 나와있지 않다.
            5
    4             6
              3         7
에서 3은  위에서부터 drop한다고 생각했을 때, 5의 왼쪽 부분에 있어야 한다. 따라서 BST를 위반한다. ( 이에대해, 문제의 서술이 부족하다는 의견이 많다. )

아무튼, 일반적으로 부모의 노드의 값이 좌측과 우측 자식 노드의 값 사이에 있음을 비교하면서 자식으로 타고내려가는 dfs는 위의 상황을 막지 못한다.

따라서, 두가지 접근 방법을 진행했는데, 첫번째는 bfs였다.
bfs를 통해 레벨별 원소들을 저장해놓고, 현재 레벨의 원소들을 이전 레벨의 원소들과 비교해서 어떤 노드의 또 좌측 혹은 우측 자식노드가 될 것인지를 파악하려 했다. → 너무 복잡

두번째는 범위를 통한 접근이다.
이 방식은 혁명적인 방법이므로 기억해두자.
다음 좌측노드는 무조건 현재 부모노드의 값보다 작은 값이 와야하고, 우측노드는 무조건 현재 부모노드의 값보다 큰 값이 와야한다는 기본 중의 기본을 이용한 방식이다. 이건 기억하기 쉽지만 dfs의 초기조건을 잘 기억하자. 첫 시작의 범위를 -inf to inf 로 두고 좁혀 나가는 방식을 이용하는 것이다. 이렇게하면 쉽게 코드를 구현 가능하다.
"""