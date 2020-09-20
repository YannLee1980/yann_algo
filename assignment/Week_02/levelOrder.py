# 429. N叉树的层序遍历
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/

# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

# 例如，给定一个 3叉树 :

# 返回其层序遍历:

# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        deque = collections.deque([root])

        while deque:
            level = []
            for _ in range(len(deque)):
                node = deque.popleft()
                level.append(node.val)
                deque.extend(node.children)
            result.append(level)

        return result