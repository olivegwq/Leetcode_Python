class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res,i,=0,0
        while n:
            res=res*2+n%2
            n//=2
            i+=1
        if i<32:
            res=res*math.pow(2,32-i)
        return int(res)
