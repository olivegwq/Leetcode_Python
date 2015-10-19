# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cur_q=[]
        next_q=[]
        TreeList=[]
        curList=[]
        level=0
        if root:
            cur_q.append(root)
        
        while cur_q:
            cur_node=cur_q[0]
            del cur_q[0]
            curList.append(cur_node.val)
            if cur_node.left:
                    next_q.append(cur_node.left)
            if cur_node.right:
                    next_q.append(cur_node.right)
            if not cur_q:
                cur_q=next_q
                next_q=[]
                TreeList.append(curList)
                curList=[]
                
        return TreeList
