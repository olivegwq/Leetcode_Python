class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        col=''
      
        while n:
            col=chr((n-1)%26+ord('A'))+col
            n=(n-(n-1)%26)/26
        
        return col
