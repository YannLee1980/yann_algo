# 144. 二叉树的前序遍历
# 给定一个二叉树，返回它的 前序 遍历。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root, traverse_path):
            if not root:
                return
            traverse_path.append(root.val)
            preorder(root.left, traverse_path)
            preorder(root.right, traverse_path)
        
        traverse_path = []
        preorder(root, traverse_path)
        return traverse_path