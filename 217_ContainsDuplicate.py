class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not len(nums):
            return False
        pool=set()
        for i in range(len(nums)):
            if nums[i] in pool:
                return True
            else:
                pool.add(nums[i])
        return False
