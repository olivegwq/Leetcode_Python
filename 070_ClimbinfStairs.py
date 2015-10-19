class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pt1,pt2=1,1
        
        for i in range(n-1):
            pt2=pt1+pt2
            pt1=pt2-pt1
        
        return pt2
