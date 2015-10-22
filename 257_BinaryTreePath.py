#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        nStack,path,cur_path=[],[],[]
        
        if not root:
            return path
        if not root.left and not root.right:
            return [str(root.val)]
        else:
            subpath1=self.binaryTreePaths(root.left)
            subpath2=self.binaryTreePaths(root.right)
            return self.CombineList(root.val,subpath1+subpath2)
    def CombineList(self, num, subpath):
        if not subpath:
            return        
        for i in range(len(subpath)):
            subpath[i]=str(num)+'->'+subpath[i]
        return subpath
