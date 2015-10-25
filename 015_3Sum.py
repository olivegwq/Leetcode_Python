class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for ia in xrange(len(nums)-2):
            if nums[ia]>0:
                break
            if ia>0 and nums[ia]==nums[ia-1]:
                continue
            ib,ic=ia+1,len(nums)-1
            while ib<ic:
                if nums[ia]+nums[ib]+nums[ic]==0:
                    res.append([nums[ia],nums[ib],nums[ic]])
                    while ib<ic and nums[ib+1]==nums[ib]: ib+=1
                    while ib<ic and nums[ic-1]==nums[ic]: ic-=1
                    ib+=1
                    ic-=1
                elif nums[ia]+nums[ib]+nums[ic]>0: 
                    ic-=1 
                else:
                    ib+=1
        return res
