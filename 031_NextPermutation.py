class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        indx=len(nums)-2
        
        while indx>=0 and nums[indx]>=nums[indx+1]:
            indx-=1
        if indx>=0: 
            p=len(nums)-1
            while nums[indx]>=nums[p]:
                p-=1
            nums[p],nums[indx]=nums[indx],nums[p]
                
        p=len(nums)-1
        q=indx+1
        
        while p>q:
            nums[p],nums[q]=nums[q],nums[p]
            p-=1
            q+=1
        return
