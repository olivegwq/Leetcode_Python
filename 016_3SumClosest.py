class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=sum(nums[0:3])
        
        for ia in range(len(nums)-2):
            if ia>0 and nums[ia]==nums[ia-1]:
                continue
            ib,ic=ia+1,len(nums)-1
            while ib<ic:
                if abs(nums[ia]+nums[ib]+nums[ic]-target)<abs(res-target):
                    res=nums[ia]+nums[ib]+nums[ic]
                if nums[ia]+nums[ib]+nums[ic]>target:
                    while ib<ic and nums[ic-1]==nums[ic]: ic-=1
                    ic-=1
                elif nums[ia]+nums[ib]+nums[ic]<target:
                    while ib<ic and nums[ib+1]==nums[ib]: ib+=1
                    ib+=1
                else:
                    break
        return res
