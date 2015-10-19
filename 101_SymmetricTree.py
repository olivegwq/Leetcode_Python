# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMirror(self,n1,n2):
        if (not n1) and (not n2):
            return True
        elif not (n1 and n2):
            return False
        else:
            return n1.val==n2.val and self.isMirror(n1.left,n2.right) and self.isMirror(n1.right,n2.left)
            
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root,root)  
