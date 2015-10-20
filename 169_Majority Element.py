
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        maj=[]
        n=len(nums)//2
        for item in nums:
            if item in dict:
                dict[item]+=1
                if dict[item]>n:
                    return item
            else:
                dict[item]=1
                if dict[item]>n:
                    return item
        return 0
