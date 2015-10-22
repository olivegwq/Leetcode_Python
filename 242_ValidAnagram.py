class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict={}
        
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for j in t:
            if j not in dict:
                return False
            elif j in dict:
                if dict[j]==1:
                    del dict[j]
                else:
                    dict[j]-=1
        if len(dict):
            return False
        else:
            return True
