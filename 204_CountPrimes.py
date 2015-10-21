class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        pool=[0,0]+[1 for i in xrange(2,n)]
        
        for i in range(2,n):
            if pool[i]:
                for j in xrange(2,(n-1)/i+1):
                    pool[j*i]=0
        return sum(pool)
