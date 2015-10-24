class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pool={}
        for ele in nums:
            if ele in pool:
                del pool[ele]
            else:
                pool[ele]=0
        res=[ele for ele in pool]
        
        return res[0]
        
