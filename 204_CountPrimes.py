class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        pool=[0,0]+[1 for i in range(2,n)]
        
        for i in range(2,n):
            if pool[i]:
                for j in range(2,(n-1)/i+1):
                    pool[j*i]=0
        return sum(pool)
