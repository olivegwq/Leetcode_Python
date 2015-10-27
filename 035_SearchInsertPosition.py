class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L,R=0,len(nums)-1
        
        while L<=R:
            M=(L+R)/2
            if nums[M]>target:
                R=M-1
            elif nums[M]<target:
                L=M+1
            else:
                return M
        return L
