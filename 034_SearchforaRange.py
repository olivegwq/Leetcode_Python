class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p,q=0,len(nums)-1
        
        if nums[q]<target or nums[p]>target:
            return [-1,-1]
        while p<=q:
            mid=(p+q)/2
            if nums[mid]<target:
                p=mid+1
            elif nums[mid]>target:
                q=mid-1
            else:
                break
        if p>q:
            return [-1,-1]
        midp,midq=mid-1,mid+1
        while p<=midp:
            if nums[(midp+p)/2]<target:
                p=(midp+p)/2+1
            else:
                midp=(midp+p)/2-1
        while q>=midq:
            if nums[(midq+q+1)/2]>target:
                q=(midq+q+1)/2-1
            else:
                midq=(midq+q+1)/2+1
        return [p,q]
