class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n%2 or n<=0:
            return False
        else:
            return self.isPowerOfTwo(n/2)
