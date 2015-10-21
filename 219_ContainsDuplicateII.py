class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        
        dict={}
        
        for i in range(len(nums)):
            if nums[i] in dict:
                if abs(i-min(dict[nums[i]]))<=k or abs(i-max(dict[nums[i]]))<=k:
                    return True
                else:
                    dict[nums[i]].append(i)
            else:
                dict[nums[i]]=[i]
        return False
