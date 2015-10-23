class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        str=str.split()   
        if len(pattern)!=len(str):
            return False
        D1,D2={},{}
        for i in range(len(pattern)):
            if pattern[i] not in D1 and str[i] not in D2:
                D1[pattern[i]]=str[i]
                D2[str[i]]=pattern[i]
            elif pattern[i] in D1 and str[i] in D2:
                if D1[pattern[i]]!=str[i] or D2[str[i]]!=pattern[i]:
                    return False
            else:
                return False
        return True
        return True
