'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
 """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        head, end =0
        for i in range(1,len(s)):
            indx=s[head:end].find(s[i])
            if indx==-1:
                end=i
            else:
                head=indx
        return len(s[head:end])+1      
                
