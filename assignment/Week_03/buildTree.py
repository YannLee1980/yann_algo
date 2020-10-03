# 105. 从前序与中序遍历序列构造二叉树
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind  = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root