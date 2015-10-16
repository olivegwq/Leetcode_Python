'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        head, end, strl =0,1,1
        for i in range(1,len(s)):
            indx=s[head:end].find(s[i])
            if indx==-1:
                end=i+1
                strl=max(strl,end-head)
            else:
                head=head+indx+1
                end=i+1
        return strl      
                
