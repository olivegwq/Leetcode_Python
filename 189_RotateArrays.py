class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k==0 or not nums:
            return
        k%=len(nums)
        nums[:]=nums[-k:]+nums[0:-k]
        return
