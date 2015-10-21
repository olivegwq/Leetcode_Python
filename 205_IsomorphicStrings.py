class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dicts,dictt={},{}
        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]]=t[i]
            elif dicts[s[i]]!=t[i]:
                return False
            if t[i] not in dictt:
                dictt[t[i]]=s[i]
            elif dictt[t[i]]!=s[i]:
                return False
        return True
                
