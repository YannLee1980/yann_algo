# 94. 二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root, traverse_path):
            if not root:
                return
            inorder(root.left, traverse_path)
            traverse_path.append(root.val)
            inorder(root.right, traverse_path)
        
        traverse_path = []
        inorder(root, traverse_path)
        return traverse_path