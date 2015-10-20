# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.right:
            return 1+self.minDepth(root.left)
        if root.right and not root.left:
            return 1+self.minDepth(root.right)
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))