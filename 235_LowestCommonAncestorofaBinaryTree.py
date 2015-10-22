# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        nstack=collections.deque()
        if not root:
            return root
        nstack.append(root)
        while nstack:
            node=nstack.popleft()
            if self.isDescendant(node.left,p) and self.isDescendant(node.left,q):
                nstack.append(node.left)
            elif self.isDescendant(node.right,p) and self.isDescendant(node.right,q):
                nstack.append(node.right)
            else:
                return node
            
        
    def isDescendant(self,par,des):
        if not par:
            return False
        elif des==par:
            return True
        else:
            return self.isDescendant(par.left,des) or self.isDescendant(par.right,des)



###################
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        a,b=sorted([p.val,q.val])
        while not a<=root.val<=b:
            root=root.left if b<root.val else root.right
        return root
