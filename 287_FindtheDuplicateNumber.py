class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow,fast=0,0
        
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            
            if slow==fast:
                break
        
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            
            if slow ==fast:
                return slow
