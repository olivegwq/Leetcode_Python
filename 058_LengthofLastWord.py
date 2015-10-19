class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        indx=len(s)-1
        while s[indx]==' ':
            indx-=1
            if indx<0:
                return 0
        indx2=s[:indx].rfind(' ')
        
        return indx-indx2
