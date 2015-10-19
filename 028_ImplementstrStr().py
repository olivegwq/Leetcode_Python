class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        head=0
        while head<=len(haystack)-len(needle):
            if haystack[head]!=needle[0]:
                head+=1
                continue
            i=0
            while i<len(needle):
                if haystack[head+i]!=needle[i]:
                    break
                i+=1
                if i==len(needle):
                    return head
            head+=1
        return -1
