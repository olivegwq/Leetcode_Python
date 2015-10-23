# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        p,q=0,n
        
        while p<q-1:
            if isBadVersion((p+q)/2):
                q=(p+q)/2
            else:
                p=(p+q)/2
        return q
