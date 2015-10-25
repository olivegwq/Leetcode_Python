class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        qualets=[]
        if not nums:
            return qualets
        for ia in xrange(len(nums)-3):
            if ia>0 and nums[ia]==nums[ia-1]:
                continue
            sub=self.threeSum(nums[ia+1:],target-nums[ia])
            if len(sub)==0:
                continue
            for ele in sub:
                ele.insert(0,nums[ia])
                qualets.append(ele)
        return qualets
    
    def threeSum(self,nums,target):
        trilets=[]
        if not nums:
            return trilets
        for ia in xrange(len(nums)-2):
            if ia>0 and nums[ia]==nums[ia-1]:
                continue
            ib,ic=ia+1,len(nums)-1
            while ib<ic:
                if nums[ia]+nums[ib]+nums[ic]==target:
                    trilets.append([nums[ia],nums[ib],nums[ic]])
                    while ib<ic and nums[ib+1]==nums[ib]: ib+=1
                    while ib<ic and nums[ic-1]==nums[ic]: ic-=1
                    ib+=1
                    ic-=1
                elif nums[ia]+nums[ib]+nums[ic]>target:
                    ic-=1
                else:
                    ib+=1
        return trilets
