class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n:
            count+=n//5
            n=n//5
        return count
