# 589. N叉树的前序遍历
# 给定一个 N 叉树，返回其节点值的前序遍历。

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def my_preorder(root, traverse_path):
            if not root:
                return
            traverse_path.append(root.val)
            for child in root.children:
                my_preorder(child, traverse_path)
        
        traverse_path = []
        my_preorder(root, traverse_path)
        return traverse_path