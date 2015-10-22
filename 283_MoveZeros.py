class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        pre,pos=0,0
        
        while pre<len(nums) and pos<len(nums):
            while nums[pre]:
                pre+=1
                if pre==len(nums):
                    return
            pos=pre
            while not nums[pos]:
                pos+=1
                if pos==len(nums):
                    return
            nums[pre],nums[pos]=nums[pos],nums[pre]
                
            pre+=1
        return
